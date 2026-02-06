import tkinter as tk
from tkinter import messagebox
import random
import db_helper

class HangmanGame:
    def __init__(self, player_name):
        self.player_name = player_name

        self.words = [
            "python", "science", "planet", "gravity",
            "computer", "biology", "physics", "atom"
        ]

        self.word = random.choice(self.words)
        self.guessed = ["_"] * len(self.word)
        self.attempts = 6
        self.used_letters = []

        self.window = tk.Toplevel()
        self.window.title("🔤 Hangman Game")
        self.window.geometry("450x400")
        self.window.configure(bg="#FDEDEC")

        tk.Label(
            self.window,
            text="🔤 Hangman",
            font=("Comic Sans MS", 18, "bold"),
            bg="#FDEDEC"
        ).pack(pady=10)

        self.word_label = tk.Label(
            self.window,
            text=" ".join(self.guessed),
            font=("Courier", 24),
            bg="#FDEDEC"
        )
        self.word_label.pack(pady=15)

        self.info_label = tk.Label(
            self.window,
            text=f"Attempts left: {self.attempts}",
            font=("Comic Sans MS", 12),
            bg="#FDEDEC"
        )
        self.info_label.pack(pady=5)

        self.entry = tk.Entry(
            self.window,
            font=("Comic Sans MS", 14),
            width=5,
            justify="center"
        )
        self.entry.pack(pady=10)

        tk.Button(
            self.window,
            text="Guess Letter",
            font=("Comic Sans MS", 12),
            command=self.guess_letter
        ).pack(pady=5)

    def guess_letter(self):
        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not letter.isalpha() or len(letter) != 1:
            messagebox.showwarning("Invalid", "Enter ONE letter only")
            return

        if letter in self.used_letters:
            messagebox.showinfo("Used", "You already guessed that letter")
            return

        self.used_letters.append(letter)

        if letter in self.word:
            for i, ch in enumerate(self.word):
                if ch == letter:
                    self.guessed[i] = letter
        else:
            self.attempts -= 1

        self.word_label.config(text=" ".join(self.guessed))
        self.info_label.config(text=f"Attempts left: {self.attempts}")

        if "_" not in self.guessed:
            messagebox.showinfo(
                "You Win!",
                "🎉 You guessed the word!\n+10 points"
            )
            db_helper.add_score(self.player_name, "Hangman", 10)
            self.window.destroy()

        elif self.attempts == 0:
            messagebox.showerror(
                "Game Over",
                f"❌ You lost!\nWord was: {self.word}"
            )
            self.window.destroy()
