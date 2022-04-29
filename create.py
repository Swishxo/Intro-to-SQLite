"""
sqlite3 is a straightforward and simple-to-use interface for interacting with SQLite databases

SQLite has the following features.

Serverless
Self-Contained
Zero-Configuration
Transactional
Single-Database

(":memory:") is to force an SQLite database to exist purely in memory. The database ceases to exist as soon as the
database connection is closed.

cursor: is a tool used to control the database

"""

# Purpose: create a list of books I may want to read

# first import the module
import sqlite3

# Make a connection
# args: ( "database.db") or (":memory:")
conn = sqlite3.connect(":memory:")

# create a cursor
c = conn.cursor()
