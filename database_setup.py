import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)")
cursor.execute("INSERT INTO users (username) VALUES ('admin')")
cursor.execute("INSERT INTO users (username) VALUES ('user1')")
conn.commit()
conn.close()
print("Database initialized.")
