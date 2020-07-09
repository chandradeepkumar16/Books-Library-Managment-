import database

user_data = """
'a' : " to add books in list" ,
'l': " to print all the books in the list",
'r': " to mark books as read",
'd': " to delete the book".
'q' : " to quit the app"

your choice : 
"""

def menu():
    database.create_book_table()
    user_input = input(user_data)
    while user_input!='q':
        if user_input == 'a':
            prompt_add_books()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_books()
        elif user_input == 'd':
            prompt_delete_books()
        else:
            print(" you enterted the wrong choice ")
        user_input = input(user_data)



def prompt_add_books():
    name = input(" enter the name of the book: ")
    author = input(" enter the author of the book: ")
    database.add_book(name, author)

def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'yes' if book['read'] else 'no'

        print(f"{book['name']} by {book['author']} , read : {read}")


def prompt_read_books():
    name= str(input(" enter the name of the book you just finished reading: "))

    database.mark_book_as_read(name)
    print("okay , done!")


def prompt_delete_books():
    name = input(" enter the book name that you wishes to delete: ")
    database.delete_book(name)
    print(f"{name} got deleted from our book store")


menu()
