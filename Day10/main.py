
MENU = """
ENTER: 
 - a to add
 - l to list
 - e to edit
 - d to delete 
 : """

def add_book(book_shelf: list):
    title = input('Title: ')
    author = input('Author: ')
    
    book = {"title": title, "author": author}
    book_shelf.append(book)

    print(book_shelf)

def empty_shelf():
    ...




SHELF = []
option = input(MENU).lower()



if option == 'a':
    add_book(SHELF)



