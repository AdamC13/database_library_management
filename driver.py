from os import system
from database_stuff import author_db, user_db, book_db

library = {'books': [], 'authors': [], 'users': []}

#<====================> Main Menu <====================>

def main():
    while True:
        system('cls')
        action = input('''

Welcome to the Library Management System!

Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit

Select an option: 
'''
        )

        if action == '1':
            book_operations()
        elif action == '2':
            user_operations()
        elif action == '3':
            author_operations()
        elif action == '4':
            break
        else:
            print("Invalid input! ")

#<====================> Book Operations <====================>

def book_operations():
    system('cls')
    user_input = input('''
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Back to Main Menu
                           
Select an option: 
'''
)
    
#    <----------> Adding a new book <---------->

    if user_input == '1':

#        ---------- Getting Book Values ----------
        title = input("\nWhat is the title of the book you will be adding? ")
        author = input(f"\nWhat is the author of {title}? ")
        isbn = input(f"\nWhat is the isbn of {title}? ")
        genre = input(f"\nWhat is the genre of {title}? ")
        publication_date = input(f"\nWhat is the publication date of {title}? ")

#        ---------- Adding the appropriate object to the library ----------
        book_db.add_book(title, genre, publication_date, isbn, author)
        input("\nThe book was successfully added to the library!")

#    <----------> Borrowing a book <---------->

    if user_input == '2':

#        ---------- Finding the book ----------
        title = input("\nWhat is the name of the book you would like to borrow? ")
        book_db.checkout_book(title)
        input("")


        


                


#    <----------> Returning a book <---------->

    if user_input == '3':

#        ---------- Finding the book ----------
        title = input("\nWhat is the name of the book you would like to return? ")

        book_db.return_book(title)
        input("")


#    <----------> Searching for a book <---------->

    if user_input == '4':

#        ---------- Finding the book ----------
        title = input("\nWhat is the name of the book you are looking for? ")

        book_db.book_details(title)
        input("")

        
#    <----------> Displaying all books <---------->

    if user_input == '5':
        print('\n')
        book_db.view_book()
        
        input("\n")


#<====================> User Operations <====================>

def user_operations():
    system('cls')
    user_input = input('''
User Operations:
1. Add a new user
2. View user details
3. Display all users
4. Back to Main Menu
                       
Select an option: 
'''
)
    
#    <----------> Adding a new user <---------->

    if user_input == '1':

#        ---------- Getting Book Values ----------
        name = input(f"\nWhat is your name? ")
        username = input(f"\nWhat would you like your username to be? ")

#        ---------- Adding the appropriate object to the library ----------
        user_db.add_user(name, username)

        input(f"\nCongrats {name}, you have been regeistered under the username: {username} ")

#    <----------> View user details <---------->

    if user_input == '2':

#        ---------- Finding the user ----------
        username = input("What is the username of the user you want to view? ")
        try:
            print("\n")
            user_db.user_details(username)
            input("")
        except:
            # If the user is not found
            input(f"Sorry, no user exists under the username: {username}")

#    <----------> Displaying all users <---------->

    if user_input == '3':
        print('\n')
        user_db.view_users()
        
        input("\n")


        
#<====================> Author Operations <====================>

def author_operations():
    system('cls')
    user_input = input('''
Author Operations:
1. Add a new author
2. View author details
3. Display all authors
4. Back to Main Menu
                       
Select an option: 
'''
)
#    <----------> Adding a new author <---------->

    if user_input == '1':

#        ---------- Getting author values ----------
        name = input(f"\nWhat is the authors name? ")
        bio = input(f"\nGive a quick biography for the author: ")

#        ---------- Adding the author to the library ----------
        author_db.add_author(name, bio)

        input(f"\nThe author {name} has been added to the library! ")

#    <----------> View author details <---------->

    if user_input == '2':

#        ---------- Finding the author ----------
        name = input("What is the name of the author you want to view? ")

        author_db.author_details(name)
        input("")


#    <----------> Displaying all authors <---------->

    if user_input == '3':
        author_db.view_authors()
        input("\n")


#<====================> Function Calls <====================>

main()