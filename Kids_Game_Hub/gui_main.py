import tkinter as tk
from tkinter import messagebox, simpledialog

from gui_guess_number import GuessNumberGame
from gui_rock_paper_scissors import RockPaperScissorsGame
import db_helper


# Create main window
root = tk.Tk()
root.title("🎮 Kids Game Hub 🎮")
root.geometry("400x400")
root.configure(bg="#FFEB99")

# Title
title = tk.Label(
    root,
    text="🎮 Kids Game Hub 🎮",
    font=("Comic Sans MS", 18, "bold"),
    bg="#FFEB99",
    fg="#333"
)
title.pack(pady=20)


# Ask player name
player_name = simpledialog.askstring(
    "Player Name",
    "Enter your name:"
)

if not player_name:
    root.destroy()
else:
    db_helper.add_player(player_name)


# Button functions
def play_guess_number():
    GuessNumberGame(player_name)



def play_rps():
    RockPaperScissorsGame(player_name)


def exit_game():
    root.destroy()


# Buttons
btn1 = tk.Button(
    root,
    text="🎯 Guess the Number",
    font=("Comic Sans MS", 12),
    width=25,
    bg="#FF9999",
    command=play_guess_number
)
btn1.pack(pady=10)

btn2 = tk.Button(
    root,
    text="✊ Rock Paper Scissors ✌️",
    font=("Comic Sans MS", 12),
    width=25,
    bg="#99CCFF",
    command=play_rps
)
btn2.pack(pady=10)

btn3 = tk.Button(
    root,
    text="❌ Exit",
    font=("Comic Sans MS", 12),
    width=25,
    bg="#CCCCCC",
    command=exit_game
)
btn3.pack(pady=20)


# Run the GUI
root.mainloop()
