"""
execute(): allow you to store data directly to the database
sql commands: CREATE TABLE, TEXT, INTEGER, IF NOT EXISTS
    CREATE TABLE: is a command used to make a database and the name of the database is lowercase
    TEXT: is the data-type of a column that stores a specific data ex:(nameOfColumn TEXT)
    INTEGER: is the data-type of a column that stores a specific data ex:(nameOfColumn INTEGER)
    IF NOT EXISTS: is command used to find out if your database is already created
"""
import sqlite3

conn = sqlite3.connect(":memory:")

cursor = conn.cursor()

# Create the table
# """: allow for the syntax to be on multiple lines making it readable
cursor.execute("""CREATE TABLE IF NOT EXISTS books 
                  (title TEXT, pages INTEGER)""")
