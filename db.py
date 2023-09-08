import sqlite3

conn = sqlite3.connect('books.sqlite')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS book")

sql_query = """
    CREATE TABLE book(
        id integer PRIMARY KEY,
        author text NOT NULL,
        language text NOT NULL,
        title text NOT NULL
    )
"""
cursor.execute(sql_query)