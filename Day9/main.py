# import requests

# response = requests.get('https://dummyjson.com/products/1')

# data = response.json()

# print(data['thumbnail'])

# with open(data['thumbnail'], mode='rb') as f:
#     image = f.raw()

# with open('testing.jpg', mode='wb') as f:
#     f.write(image)

# data = """{
#   "id": 11,
#   "title": "perfume Oil",
#   "description": "Mega Discount, Impression of A...",
#   "price": 13,
#   "discountPercentage": 8.4,
#   "rating": 4.26,
#   "stock": 65,
#   "brand": "Impression of Acqua Di Gio",
#   "category": "fragrances",
#   "thumbnail": "https://i.dummyjson.com/data/products/11/thumbnail.jpg",
#   "images": [
#     "https://i.dummyjson.com/data/products/11/1.jpg",
#     "https://i.dummyjson.com/data/products/11/2.jpg",
#     "https://i.dummyjson.com/data/products/11/3.jpg",
#     "https://i.dummyjson.com/data/products/11/thumbnail.jpg"
#   ]
# }"""

# import json

# new_data = json.loads(data)
# When working with valid json type in string
# Use json.loads() -> convert from json to python type
# Use json.dumps() -> convert from python type to json

# whe working with open() of json file obj
# Use json.load() -> convert from json to python type
# Use json.dump() -> convert from python type to json

# print(type(new_data))

# print(type(data))



# class Animal:
#     def __init__(self, color, size):
#         self.color = color
#         self.size = size

#     def eat(self):
#         return "Eating..."

# class Fish(Animal):
#     def __init__(self, color, size, tp):
#         super().__init__(color, size)
#         self.type = tp



# class Dog(Animal):
#     def __init__(self, color, size, legs):
#         super().__init__(color, size)
#         self.legs = legs

# class GermanShepard(Dog):
#     pass

# d1 = Dog('blue', 12, 4)
# print(d1.eat())

# f1 = Fish('green', 4, 'Big Fish')
# print(f1.type)




# a1 = Animal('red', 23.4)


# print(a1.color)
# print(a1.size)

# print(a1.eat())


# BOOKSTORE APP

# {
#     'title': 'Think Big',
#     'author': 'Ben Carson',
#     'ISBN': '234235645KJS',
#     'description': 'Book by Ben Carson'
# }

import backend as bk


def main():
    USER_PROMPT = """
    --------------------
    | HASEEB BOOKSTORE |
    --------------------
    What do you wanna do: 
    TYPE: 
        -a --> add a book to shelf
        -l --> list all available books
        -e --> edit a book
        -r --> read a book
        -d --> delete a book

        :::: """

    shelf = []

    option = input(USER_PROMPT).lower()

    while option != 'q':
        if option == 'a':
            bk.handle_add_to_shelf(shelf)
        elif option == 'l':
            bk.display_all_books(shelf)
        elif option == 'e':
            pass
        elif option == 'r':
            pass
        elif option == 'd':
            pass
        else:
            print('Invalid option. Try again.')
            option = input(USER_PROMPT).lower()
        
        option = input(USER_PROMPT).lower()



main()
























