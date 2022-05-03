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
print("Previous Table: ")
print(data)

# delete data from  table
cursor.execute("DELETE FROM books WHERE title='Are You My Mother'")
# commit changes to table book
conn.commit()

# select updated table book
cursor.execute("SELECT * FROM books")
# retrieve data from table
data = cursor.fetchall()

print("UPDATED TABLE: ")
print(data)
