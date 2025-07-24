import sqlite3

def log_trip(from_city, destination_city, date_from, date_to, interests, result):
    conn = sqlite3.connect("trip_logs.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO trips (from_city, destination_city, date_from, date_to, interests, result)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (from_city, destination_city, date_from, date_to, interests, result))
    conn.commit()
    conn.close()
