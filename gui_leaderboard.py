import tkinter as tk
import db_helper

class Leaderboard:
    def __init__(self, game=None):
        self.window = tk.Toplevel()
        self.window.geometry("350x350")

        if game:
            self.window.title(f"🏆 {game} Leaderboard")
            title_text = f"🏆 {game} Leaderboard"
            scores = db_helper.get_leaderboard(game)
        else:
            self.window.title("🏆 Overall Leaderboard")
            title_text = "🏆 Overall Leaderboard"
            scores = db_helper.get_overall_leaderboard()

        tk.Label(
            self.window,
            text=title_text,
            font=("Comic Sans MS", 16, "bold")
        ).pack(pady=10)

        if not scores:
            tk.Label(
                self.window,
                text="No scores yet",
                font=("Comic Sans MS", 12)
            ).pack(pady=20)
            return

        for i, (name, score) in enumerate(scores, start=1):
            tk.Label(
                self.window,
                text=f"{i}. {name} — {score} pts",
                font=("Comic Sans MS", 12)
            ).pack(pady=5)
