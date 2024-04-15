from .connect_db import connect_db

conn = connect_db()
cursor = conn.cursor()

def add_author(name, bio):
    author = (name, bio)
    query = "INSERT INTO Authors (name, biography) VALUES (%s ,%s)"
    cursor.execute(query, author)
    conn.commit()

def view_authors():
    query = "SELECT name FROM Authors"

    cursor.execute(query)
    for row in cursor.fetchall():
        name = str(row)
        char_remove = "(,')"
        for char in char_remove:
            name = name.replace(char, '')
        
        print(name)

def author_details(author):
    query = f'SELECT name, biography FROM library_management.authors WHERE name = "{author}"'
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
