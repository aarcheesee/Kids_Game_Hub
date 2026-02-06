import tkinter as tk
from tkinter import messagebox
import db_helper

class GameHistory:
    def __init__(self, player_name):
        self.player_name = player_name

        self.window = tk.Toplevel()
        self.window.title("📜 Game History")
        self.window.geometry("500x400")

        title = tk.Label(
            self.window,
            text=f"📜 {player_name}'s Game History",
            font=("Comic Sans MS", 16, "bold")
        )
        title.pack(pady=10)

        history = db_helper.get_player_history(player_name)

        if not history:
            messagebox.showinfo(
                "No History",
                "No games played yet!"
            )
            self.window.destroy()
            return

        frame = tk.Frame(self.window)
        frame.pack(pady=10)

        headers = ["Game", "Score", "Date"]
        for i, h in enumerate(headers):
            tk.Label(
                frame,
                text=h,
                font=("Comic Sans MS", 12, "bold"),
                width=15,
                borderwidth=1,
                relief="solid"
            ).grid(row=0, column=i)

        for r, row in enumerate(history, start=1):
            for c, value in enumerate(row):
                tk.Label(
                    frame,
                    text=value,
                    width=15,
                    borderwidth=1,
                    relief="solid"
                ).grid(row=r, column=c)
