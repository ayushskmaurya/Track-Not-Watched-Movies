import sqlite3

conn = sqlite3.connect('watched_movies.db')
conn.execute('CREATE TABLE movies (name varchar(100) NOT NULL UNIQUE)')
conn.close()
print("Database and table created successfully.")
