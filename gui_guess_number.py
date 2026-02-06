import tkinter as tk
from tkinter import messagebox
import random
import db_helper

class GuessNumberGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.secret = random.randint(1, 20)

        self.window = tk.Toplevel()
        self.window.title("🎯 Guess the Number")
        self.window.geometry("350x250")

        tk.Label(
            self.window,
            text="Guess a number between 1 and 20",
            font=("Comic Sans MS", 12)
        ).pack(pady=15)

        self.entry = tk.Entry(self.window, font=("Comic Sans MS", 12))
        self.entry.pack(pady=10)

        tk.Button(
            self.window,
            text="Guess",
            font=("Comic Sans MS", 11),
            command=self.check_guess
        ).pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a number")
            return

        if guess == self.secret:
            messagebox.showinfo(
                "Correct!",
                "🎉 You guessed it right!\n+5 points"
            )
            db_helper.add_score(self.player_name, "Guess Number", 10)

            self.window.destroy()
        elif guess < self.secret:
            messagebox.showinfo("Try Again", "Too low ⬇️")
        else:
            messagebox.showinfo("Try Again", "Too high ⬆️")
