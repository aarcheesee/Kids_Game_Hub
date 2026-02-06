import tkinter as tk
from tkinter import messagebox
import random
import db_helper

# ----------------- SUDOKU LOGIC -----------------

def is_safe(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def generate_full_board():
    board = [[0] * 9 for _ in range(9)]

    def fill():
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_safe(board, r, c, num):
                            board[r][c] = num
                            if fill():
                                return True
                            board[r][c] = 0
                    return False
        return True

    fill()
    return board


def generate_puzzle():
    solution = generate_full_board()
    puzzle = [[solution[r][c] if random.random() < 0.4 else 0
            for c in range(9)] for r in range(9)]
    return puzzle, solution

# ----------------- GUI -----------------

class SudokuGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.puzzle, self.solution = generate_puzzle()

        self.window = tk.Toplevel()
        self.window.title("🧩 Sudoku")
        self.window.geometry("500x600")

        self.entries = [[None]*9 for _ in range(9)]

        grid = tk.Frame(self.window)
        grid.pack(pady=10)

        for r in range(9):
            for c in range(9):
                e = tk.Entry(
                    grid,
                    width=2,
                    font=("Arial", 18),
                    justify="center"
                )
                e.grid(row=r, column=c, padx=2, pady=2)

                if self.puzzle[r][c] != 0:
                    e.insert(0, str(self.puzzle[r][c]))
                    e.config(state="disabled")

                self.entries[r][c] = e

        tk.Button(
            self.window,
            text="Check Solution",
            font=("Comic Sans MS", 12),
            command=self.check_solution
        ).pack(pady=10)

        tk.Button(
            self.window,
            text="💡 Hint",
            font=("Comic Sans MS", 12),
            command=self.give_hint
        ).pack(pady=5)

    def give_hint(self):
        for r in range(9):
            for c in range(9):
                if self.puzzle[r][c] == 0:
                    entry = self.entries[r][c]

                    if entry.get() == "":
                        entry.insert(0, str(self.solution[r][c]))
                        entry.config(fg="blue")

                        messagebox.showinfo(
                            "Hint",
                            "💡 A correct number has been filled!"
                        )
                        return

        messagebox.showinfo(
            "Hint",
            "No empty cells left!"
        )

    def check_solution(self):
        for r in range(9):
            for c in range(9):
                if self.puzzle[r][c] == 0:
                    val = self.entries[r][c].get()
                    if not val.isdigit() or int(val) != self.solution[r][c]:
                        messagebox.showerror(
                            "Incorrect",
                            "❌ Solution is not correct yet"
                        )
                        return

        messagebox.showinfo(
            "Correct!",
            "🎉 Sudoku Solved!\n+10 points"
        )
        db_helper.add_score(self.player_name, "Sudoku", 10)
        self.window.destroy()
