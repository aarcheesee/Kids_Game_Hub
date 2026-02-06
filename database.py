import sqlite3

conn = sqlite3.connect("gamehub.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    total_score INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
