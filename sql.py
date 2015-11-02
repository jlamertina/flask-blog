# sql.py - Create a SQLite3 table and populate it with data
import sqlite3

# Initialize tuples of dummy blog data that we'll insert in a database table
blog_data = (
    ("Good","I\'m good."),
    ("Well","I\'m well."),
    ("Excellent","I\'m excellent."),
    ("Okay","I\'m okay.")
)

# Create a new database, connect, and initialize a table of data
with sqlite3.connect("blog.db") as myConnection:
    # Create a cursor object for submitting SQL commands on the database
    c = myConnection.cursor()
    # create the table
    c.execute("DROP TABLE IF EXISTS posts")
    c.execute("CREATE TABLE posts(title TEXT, post TEXT)")
    c.executemany("INSERT INTO posts VALUES(?,?)", blog_data)
    myConnection.commit()
    