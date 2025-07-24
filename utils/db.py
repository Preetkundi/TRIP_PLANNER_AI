import sqlite3

def init_db():
    conn = sqlite3.connect("trip_logs.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS trips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_city TEXT,
        destination_city TEXT,
        date_from TEXT,
        date_to TEXT,
        interests TEXT,
        result TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()
