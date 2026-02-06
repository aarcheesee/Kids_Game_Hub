import sqlite3

DB_NAME = "gamehub.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def setup_db():
    conn = get_connection()
    cur = conn.cursor()

    # Players table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Scores table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT NOT NULL,
        game TEXT NOT NULL,
        score INTEGER NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def add_player(name):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT OR IGNORE INTO players (name) VALUES (?)",
            (name,)
        )
        conn.commit()
    finally:
        conn.close()


def add_score(player_name, game, score):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO scores (player_name, game, score) VALUES (?, ?, ?)",
        (player_name, game, score)
    )

    conn.commit()
    conn.close()


def get_scores():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT player_name, game, score, created_at FROM scores"
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def get_player_history(player_name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT game, score, created_at
        FROM scores
        WHERE player_name = ?
        ORDER BY created_at DESC
    """, (player_name,))

    rows = cur.fetchall()
    conn.close()
    return rows
