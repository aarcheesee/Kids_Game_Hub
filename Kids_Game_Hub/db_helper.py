import sqlite3

def connect():
    return sqlite3.connect("gamehub.db")

def add_player(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO players (name, total_score) VALUES (?, ?)",
        (name, 0)
    )
    conn.commit()
    conn.close()

def add_score(name, score):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE players SET total_score = total_score + ? WHERE name = ?",
        (score, name)
    )
    conn.commit()
    conn.close()

def get_leaderboard():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, total_score FROM players ORDER BY total_score DESC LIMIT 5"
    )
    data = cursor.fetchall()
    conn.close()
    return data
