


def handle_add_to_shelf(shelf):
    book = {}
    book['title'] = input("Enter the book title: ")
    book['author'] = input("Enter the name of the auther: ")
    book['ISBN'] = input("Enter the ISBN of the book: ")
    book['description'] = input("Enter the description of the book: ")

    shelf.append(book)
    display_all_books(shelf)



def display_all_books(shelf):
    books = [f"{book['title']} by {book['author']}"  for book in shelf]
    print()
    num = 1
    for book in books:
        print(f'{num}. {book}')
        num += 1
    print()
    print("Number of books in the shelf: ", len(books))
