import tkinter as tk
from tkinter import messagebox
import random
import db_helper


class GuessNumberGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.number = random.randint(1, 10)
        self.attempts = 3

        self.window = tk.Toplevel()
        self.window.title("🎯 Guess the Number")
        self.window.geometry("350x300")
        self.window.configure(bg="#FFF3CD")

        title = tk.Label(
            self.window,
            text="🎯 Guess the Number",
            font=("Comic Sans MS", 16, "bold"),
            bg="#FFF3CD"
        )
        title.pack(pady=10)

        self.info = tk.Label(
            self.window,
            text="Guess a number between 1 and 10",
            font=("Comic Sans MS", 11),
            bg="#FFF3CD"
        )
        self.info.pack(pady=5)

        self.entry = tk.Entry(
            self.window,
            font=("Comic Sans MS", 12),
            justify="center"
        )
        self.entry.pack(pady=10)

        self.attempt_label = tk.Label(
            self.window,
            text=f"Attempts left: {self.attempts}",
            font=("Comic Sans MS", 10),
            bg="#FFF3CD"
        )
        self.attempt_label.pack(pady=5)

        guess_btn = tk.Button(
            self.window,
            text="Guess 🎲",
            font=("Comic Sans MS", 11),
            bg="#A3D8F4",
            command=self.check_guess
        )
        guess_btn.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("Oops!", "Please enter a number!")
            return

        if guess == self.number:
            messagebox.showinfo("🎉 You Win!", "Correct guess! +10 points")
            db_helper.add_score(self.player_name, 10)
            self.window.destroy()

        else:
            self.attempts -= 1
            if self.attempts == 0:
                messagebox.showerror(
                    "😢 Game Over",
                    f"You lost! Number was {self.number}"
                )
                self.window.destroy()
            else:
                messagebox.showinfo("Try Again", "Wrong guess!")
                self.attempt_label.config(
                    text=f"Attempts left: {self.attempts}"
                )
                self.entry.delete(0, tk.END)
