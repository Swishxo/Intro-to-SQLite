import sqlite3

conn = sqlite3.connect(":memory:")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS books 
                  (title TEXT, 
                  pages INTEGER)""")


books = [
    ("Going to Meet the Man", 15),
    ("Are You My Mother", 23),
    ("The Giver", 233),
]

cursor.executemany("INSERT INTO books VALUES (?, ?)", books)
conn.commit()

cursor.execute('SELECT * FROM books')


data = cursor.fetchall()


print(data)