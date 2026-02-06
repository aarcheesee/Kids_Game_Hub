import tkinter as tk
from tkinter import messagebox
import random
import db_helper

class RockPaperScissorsGame:
    def __init__(self, player_name):
        self.player_name = player_name

        self.window = tk.Toplevel()
        self.window.title("✊ Rock Paper Scissors ✌️")
        self.window.geometry("360x300")

        tk.Label(
            self.window,
            text="Choose one",
            font=("Comic Sans MS", 14, "bold")
        ).pack(pady=15)

        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=10)

        for choice in ["rock", "paper", "scissors"]:
            tk.Button(
                btn_frame,
                text=choice.capitalize(),
                width=12,
                font=("Comic Sans MS", 11),
                command=lambda c=choice: self.play(c)
            ).pack(pady=5)

    def play(self, user_choice):
        computer_choice = random.choice(
            ["rock", "paper", "scissors"]
        )

        if user_choice == computer_choice:
            result = "It's a Tie 😐"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            result = "🎉 You Win!\n+5 points"
            db_helper.add_score(self.player_name, "Rock Paper Scissors", 5)

        else:
            result = "😢 You Lose!"

        messagebox.showinfo(
            "Result",
            f"You chose: {user_choice}\n"
            f"Computer chose: {computer_choice}\n\n"
            f"{result}"
        )
