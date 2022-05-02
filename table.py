"""
execute(): allow you to store data directly to the database
sql commands: CREATE TABLE, TEXT, INTEGER
    CREATE TABLE: is a command used to make a database and the name of the database is lowercase
    TEXT: is the data-type of a column that stores a specific data

"""
import sqlite3

conn = sqlite3.connect(":memory:")

cursor = conn.cursor()

# Create the table
cursor.execute("CREATE TABLE books (title TEXT, pages INTEGER)")