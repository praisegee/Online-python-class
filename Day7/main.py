

# var = {"name": "Haseeb", "age": 16, "hobby": "coding"}

# print(len(var))

# for i in var:
#     print(i)

# you can use for over any sequeces type
# - str
# - list
# - tuple
# - dict

# name = "Haseeb"


# for letter in name:
#     if letter == "s":
#         break
#     print(letter)


# List comprehension
# numbers = [i for i in range(1, 11)]


# Alternative
# numbers = []

# for i in range(1, 11):
#     numbers.append(i)

# print(numbers)




# CRUD -> Create, Read, Update and Delete

# person = {"name": "Haseeb", "age": 16, "hobby": "coding"} # Create

# print("Items: ", person.items())
# print("Keys: ", person.keys())
# print("Values: ", person.values())

# for key in person.keys():
#     print(key)

# for key in person.values():
#     print(key)


# Unpacking
# name, *ages = ("Haseeb", 16, 23, 45, 57, 98, 34)

# print(name)
# print(ages)

# a, b = 1, {"name": "Good"}

# print(a)
# print(b)

# for key, val in person.items():
#     print(key)
#     print(val)


# person["hobby"] = "swimming" # Update

# name1 = person["name"]
# name2 = person.get("name", "Something")

# print(name1)
# print(name2)
# print(person)
# person.clear()
# print(dir(person))
# print(person)
# print(person)

# person.update({"next": 17})

# print(person)

# person2 = person.copy()

# print("Person 2: ", person2)

# numbers = {}

# for i in range(1, 11):
#     numbers.update({i: i**2})

# numbers = {i**2: i for i in range(1, 11)}


# print(numbers)




# Functions



# def greet(name): # name -> parameter
#     print(f"Hello {name}")
#     print("How are you?")

#     return 123
#     print("ajksdhjkasd") # Python will not execute this


# print(greet("HPG")) # "HPG" -> argument

# def add(x, y):
#     print("skmdfhksdjfjks")
#     a = x + y
#     return a

# def genarate(length):
#     for i in range(length):


# def sub(a, b):
#     print("skmdfhksdjfjks")
#     return a - b


# x = 534
# y = 934
# z = add(x, y)

# print(z)
# a = 5
# def do_something():
#     print("INner: ", a)
#     # a = "Good"
#     # print(a)  # SCOPE
#     # print(b)

#     def another():
#         print(a)
#         b = "asdf"

# # print(a)

# do_something()



# Defaul parameters

# def greet(name, hobby, age=16):
#     print(f"Hi {name}, {hobby} You're {age} years old!")

# greet("Haseeb", 18)

# JSON -> JavaScript Object Notation





    

























