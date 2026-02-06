import tkinter as tk
import db_helper

class ScoreBoard:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("🏆 Scoreboard")
        self.window.geometry("350x400")

        title = tk.Label(
            self.window,
            text="🏆 Scoreboard",
            font=("Comic Sans MS", 16, "bold")
        )
        title.pack(pady=15)

        scores = db_helper.get_all_scores()

        frame = tk.Frame(self.window)
        frame.pack(pady=10)

        header1 = tk.Label(frame, text="Player", font=("Comic Sans MS", 12, "bold"), width=15)
        header1.grid(row=0, column=0)

        header2 = tk.Label(frame, text="Score", font=("Comic Sans MS", 12, "bold"), width=10)
        header2.grid(row=0, column=1)

        for i, (name, score) in enumerate(scores, start=1):
            tk.Label(frame, text=name, font=("Comic Sans MS", 11)).grid(row=i, column=0)
            tk.Label(frame, text=str(score), font=("Comic Sans MS", 11)).grid(row=i, column=1)
