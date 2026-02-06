import tkinter as tk
from tkinter import ttk
import db_helper
db_helper.setup_db()

from tkinter import simpledialog

from gui_guess_number import GuessNumberGame
from gui_rock_paper_scissors import RockPaperScissorsGame
from gui_sudoku import SudokuGame 
from gui_hangman import HangmanGame
from gui_leaderboard import Leaderboard
from gui_scoreboard import ScoreBoard
from gui_history import GameHistory



import db_helper



root = tk.Tk()
root.title("🎮 Kids Game Hub 🎮")
root.geometry("420x450")
root.configure(bg="#FFEB99")

player_name = simpledialog.askstring(
    "Player Name",
    "Enter your name:"
)

if not player_name:
    root.destroy()

title = tk.Label(
    root,
    text="🎮 Kids Game Hub 🎮",
    font=("Comic Sans MS", 18, "bold"),
    bg="#FFEB99"
)
title.pack(pady=20)

def play_guess():
    GuessNumberGame(player_name)

def play_rps():
    RockPaperScissorsGame(player_name)
    
def play_sudoku():
    SudokuGame(player_name)
    
def play_hangman():
    HangmanGame(player_name)

def show_guess_leaderboard():
    Leaderboard("Guess Number")

def show_rps_leaderboard():
    Leaderboard("Rock Paper Scissors")

def show_sudoku_leaderboard():
    Leaderboard("Sudoku")

def show_hangman_leaderboard():
    Leaderboard("Hangman")


def view_scores():
    ScoreBoard()

def show_overall_leaderboard():
    Leaderboard()
    
def show_history():
    GameHistory(player_name)

def open_leaderboard():
    leaderboard = tk.Toplevel()
    leaderboard.title("🏆 Leaderboard")
    leaderboard.geometry("500x300")

    columns = ("Player", "Game", "Score")

    tree = ttk.Treeview(leaderboard, columns=columns, show="headings")
    tree.heading("Player", text="Player")
    tree.heading("Game", text="Game")
    tree.heading("Score", text="Score")

    tree.pack(fill="both", expand=True)

    scores = db_helper.get_all_scores()

    for row in scores:
        tree.insert("", tk.END, values=row)


btn_style = {
    "font": ("Comic Sans MS", 12),
    "width": 28,
    "pady": 5
}
tk.Button(root, text="🎯 Guess the Number",
        command=play_guess,
          **btn_style).pack()

tk.Button(root, text="✊ Rock Paper Scissors",
        command=play_rps,
          **btn_style).pack()

tk.Button(root, text="🧩 Sudoku",
        command=play_sudoku,
          **btn_style).pack()

btn4 = tk.Button(
    root,
    text="🔤 Hangman",
    font=("Comic Sans MS", 12),
    width=25,
    bg="#FADBD8",
    command=play_hangman
)
btn4.pack(pady=10)

tk.Button(
    root,
    text="🏆 Guess Number Leaderboard",
    width=30,
    command=show_guess_leaderboard
).pack(pady=3)

tk.Button(
    root,
    text="🏆 RPS Leaderboard",
    width=30,
    command=show_rps_leaderboard
).pack(pady=3)

tk.Button(
    root,
    text="🏆 Sudoku Leaderboard",
    width=30,
    command=show_sudoku_leaderboard
).pack(pady=3)

tk.Button(
    root,
    text="🏆 Hangman Leaderboard",
    width=30,
    command=show_hangman_leaderboard
).pack(pady=3)

tk.Button(
    root,
    text="🏆 View Scoreboard",
    command=open_leaderboard
).pack(pady=10)

btn_leaderboard = tk.Button(
    root,
    text="🏆 View Leaderboard",
    font=("Comic Sans MS", 12),
    width=25,
    bg="#FFD966",
    command=open_leaderboard
)
btn_leaderboard.pack(pady=10)

btn4 = tk.Button(
    root,
    text="📜 Game History",
    font=("Comic Sans MS", 12),
    width=25,
    bg="#B5EAD7",
    command=show_history
)
btn4.pack(pady=10)


tk.Button(root, text="❌ Exit",
        command=root.destroy,
          **btn_style).pack(pady=15)

db_helper.setup_db()

root.mainloop()