import sqlite3

conn = sqlite3.connect(":memory:")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS books 
                  (title TEXT, 
                  pages INTEGER)""")

# another way to insert values into your column is to create a list of tuples
books = [
    ("Going to Meet the Man", 15),
    ("Are You My Mother", 23),
    ("The Giver", 233),
]
# insert table
# (?, ?): subs for the book name and the book page
cursor.executemany("INSERT INTO books VALUES (?, ?)", books)
conn.commit()


# retrieve all data
cursor.execute('SELECT * FROM books')


# retrieve specified data
# cursor.execute('SELECT * FROM books WHERE title="Going to Meet the Man"')


# fetchone(): gets the data from one row of table column, get a tuple
# fetchall(): gets all rows from the table, get a list of tuples
data = cursor.fetchall()

# prints a tuple
print(data)