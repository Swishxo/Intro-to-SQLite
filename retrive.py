import sqlite3

conn = sqlite3.connect(":memory:")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS books 
                  (title TEXT, 
                  pages INTEGER)""")

cursor.execute("INSERT INTO books VALUES ('Going To Meet The Man?', 15)")

conn.commit()

