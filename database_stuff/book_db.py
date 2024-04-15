from .connect_db import connect_db
from random import getrandbits

# CREATE TABLE books (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(255) NOT NULL,
#     genre VARCHAR(30),
#     isbn VARCHAR(13) NOT NULL,
#     publication_date DATE,
#     availability BOOLEAN DEFAULT 1,
#     FOREIGN KEY (author_id) REFERENCES authors(id)
# );
conn = connect_db()
cursor = conn.cursor()

def add_book(title, genre, publication_date, isbn, author):
    user = (title, genre, publication_date,  isbn, True, author)
    query = "INSERT INTO Books (title, genre, publication_date, isbn, availability, author) VALUES (%s ,%s, %s, %s, %s, %s)"
    cursor.execute(query, user)
    conn.commit()

def view_book():
    query = "SELECT title FROM Books"

    cursor.execute(query)
    for row in cursor.fetchall():
        username = str(row)
        print(username)

def book_details(title):
    query = f'SELECT title, author, genre, publication_date, isbn, availability FROM library_management.Books WHERE title = "{title}"'
    cursor.execute(query)
    for row in cursor.fetchall():
        for value in row:
            if value == 1:
                print("Available")
            elif value == 0:
                print("Not Available")
            else:
                print(value)

def checkout_book(title):
    query = f'SELECT availability FROM library_management.Books WHERE title = "{title}"'
    cursor.execute(query)
    book_availability = cursor.fetchall()
    if book_availability == []:
        print("\nThat book is not in the library.")
        return
    for row in book_availability:
        print(row)
        for value in row:
            print(value)
            if value == 0:
                print("That book is not available.")
                return
            elif value == 1:
                query = "USE library_management"
                cursor.execute(query)

                query = f'UPDATE Books SET availability = False WHERE title = "{title}"'
                cursor.execute(query)
                conn.commit()

                print("The book has been checked out!")
                return

def return_book(title):
    query = f'SELECT availability FROM library_management.Books WHERE title = "{title}"'
    cursor.execute(query)
    book_availability = cursor.fetchall()
    if book_availability == []:
        print("\nThat book is not in the library.")
        return
    for row in book_availability:
        print(row)
        for value in row:
            print(value)
            if value == 1:
                print("That book was already returned.")
                return
            elif value == 0:
                #query = "USE library_management"
                #cursor.execute(query)

                query = f'UPDATE Books SET availability = True WHERE title = "{title}"'
                cursor.execute(query)
                conn.commit()

                print("The book has been returned!")
                return




    

