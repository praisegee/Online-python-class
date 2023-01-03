# Exception

# print(age)

# Types of errors in oython
# 1. SyntaxError
# 2. Exception




# a = input("First Num: ")
# b = input("Second Num: ")

# try:
#     print(a /b)
# except TypeError:
#     print("We need an integer")




# dictionary = {"eat": "to eat something", "jump": "to jump up"}


# word = input("Enter a word: ")

# try:
#     meaning = dictionary[word]
# except KeyError:
#     print("Invalid word: try again!")
# else:
#     print("Meaning: ", meaning)
# finally:
#     print("No matter how.. This will run..")

# book = {"name": "A book", "author": "Haseeb"}


# class NotHaseebError(Exception):
#     def __init__(self, msg, *args, **kwargs):
#         super().__init__(msg, *args, **kwargs)


# name = input("Enter your name: ")

# if name == "PG":
#     raise NotHaseebError('Your name is not Haseeb')
# else:
#     print("Name: ", name)



# When woking with file
# absolute path = /home/praisegod/Haseeb/Day11/simple.txt
# relative path = ../simple.txt
# f = open('dajhgjgjta.txt', mode='r')

# f.write(" Haseeb")
# print(f.read())
# print(f.readlines())
# print(dir(f))

# f.close()

# with open('../README.md', 'r') as f:
#     print(f.read())


import requests

url = 'https://api.github.com/users/praisegee/repos'


response = requests.delete(url)

data = response.json()

#Print all the repo name
for repo in data:
    print(repo['name'])







# print(dir(f))





