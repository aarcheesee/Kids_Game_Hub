import tkinter as tk
from tkinter import messagebox
import random
import db_helper

class RockPaperScissorsGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.window = tk.Toplevel()
        self.window.title("✊ Rock Paper Scissors ✌️")
        self.window.geometry("400x350")
        self.window.configure(bg="#E8F6F3")

        title = tk.Label(
            self.window,
            text="✊ Rock Paper Scissors ✌️",
            font=("Comic Sans MS", 16, "bold"),
            bg="#E8F6F3"
        )
        title.pack(pady=15)

        info = tk.Label(
            self.window,
            text="Choose one:",
            font=("Comic Sans MS", 12),
            bg="#E8F6F3"
        )
        info.pack(pady=10)

        btn_frame = tk.Frame(self.window, bg="#E8F6F3")
        btn_frame.pack(pady=10)

        rock_btn = tk.Button(
            btn_frame,
            text="✊ Rock",
            font=("Comic Sans MS", 11),
            width=10,
            bg="#FADBD8",
            command=lambda: self.play("rock")
        )
        rock_btn.grid(row=0, column=0, padx=10)

        paper_btn = tk.Button(
            btn_frame,
            text="✋ Paper",
            font=("Comic Sans MS", 11),
            width=10,
            bg="#D6EAF8",
            command=lambda: self.play("paper")
        )
        paper_btn.grid(row=0, column=1, padx=10)

        scissors_btn = tk.Button(
            btn_frame,
            text="✌️ Scissors",
            font=("Comic Sans MS", 11),
            width=10,
            bg="#D5F5E3",
            command=lambda: self.play("scissors")
        )
        scissors_btn.grid(row=0, column=2, padx=10)

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a Tie 😐"

        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            result = "🎉 You Win! +5 points"
            db_helper.add_score(self.player_name, 5)

        else:
            result = "😢 You Lose!"

        messagebox.showinfo(
            "Result",
            f"You chose: {user_choice}\n"
            f"Computer chose: {computer_choice}\n\n"
            f"{result}"
        )
