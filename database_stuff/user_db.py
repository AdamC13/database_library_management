from .connect_db import connect_db
from random import getrandbits

conn = connect_db()
cursor = conn.cursor()

def add_user(name, username):
    user = (name, username, str(getrandbits(30)))
    query = "INSERT INTO Users (name, username, library_id) VALUES (%s ,%s, %s)"
    cursor.execute(query, user)
    conn.commit()

def view_users():
    query = "SELECT username FROM Users"

    cursor.execute(query)
    for row in cursor.fetchall():
        username = str(row)
        print(username)

def user_details(username):
    query = f'SELECT username, name, library_id FROM library_management.users WHERE username = "{username}"'
    cursor.execute(query)
    for row in cursor.fetchall():
        print(str(row))
