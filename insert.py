"""

"""

import sqlite3

conn = sqlite3.connect(":memory:")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS books 
                  (title TEXT, 
                  pages INTEGER)""")

# insert data into database
# use sqlite command: INSERT INTO tableName VALUES (columns you provided for the data base)
cursor.execute("INSERT INTO books VALUES ('Going To Meet The Man?', 15)")

# used conn obj to insert data to the table
conn.commit()
