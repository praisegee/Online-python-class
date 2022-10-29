

# created = 1234

# pin = int(input("Enter a pin: "))

# while pin != created:
#     print("Incorrect!...")
#     pin = int(input("Enter a pin: "))

# print("Correct!")



#TODAY

# Function

# def add(x, y):
#     addition = x + y
#     print(addition)

# DRY --> Don't Repeat Yourself

# def greet(name):
#     return f"""
#             Hello {name}
#             How are you?
#             print("Hope you'r good?
#            """


# print("Result of the function is : ", greet("Hasseb"))


# def add(x, y):
#     # x = 3, y = 5
#     print(x + y) # 8


# print(add(3, 5))# -->  8


# When returning to a function, 
# return does 2 things
## - it breakes or terminate the execution of that function
## - it changes the value of the function to the operand of return keywork
## - if a function doesn't have a return statement with value, it returns None..

# def greet():
#     print("Hello")
#     print("Hi")
#     print("Hi")
#     print("Hi")
#     return

# greet()


# def _abs(x):
#     if x < 0:
#         return x * -1
#     return x

# print(_abs(-18))



# x = 5
# # Global scope
# def change():
#     # local scope | function scope
#     y = 6
#     print("Inner X: ", x)
#     print("Inner Y: ", y)

#     return 23

# print(change())
# print("Outter X: ", x)


# Tuple Unpacking

# *a, b = 2, 4, 6

# print(a)
# print(b)

#          Key      Value   Key    value
# person = {"name": "Haseeb", "age": 16, "hobby": "coding"}

# for x, y in person.items():
#     print("X: ", x)
#     print("Y: ", y)

# print(person["age"])
# print(type(person))
# print(dir(person))
# print(person.items())

# print(type(items))


# students = [
#     {
#         "name": "Haseeb",
#         "age": 16
#     },
#     {
#         "name": "Scott",
#         "age": 17
#     },
#     {
#         "name": "Jason",
#         "age": 15
#     }
# ]

# for student in students:
#     message = f"Hi {student['name']}, you're {student['age']}"
#     print(message)


## Arithmection functions

def add(x, y):
    return x + y

def sub(x, y):
    return x - y


operation = {
    "+": add,
    "-": sub
}

choice = input("What do you wanna do? (+, -): or q to quit ") # choice = "+"

while choice != "q":
    num1 = int(input("Enter 1st number: ")) # num1 = 4
    num2 = int(input("Enter 2nd number: "))
    result = operation[choice](num1, num2) # (operation["+"]) --> add(4, 6)
    print(result)
    print()

    choice = input("What do you wanna do? (+, -): or q to quit: ") # choice = "+"






 # Assignment -  A program to check If a number is Even or Odd

# Function prototype 

# def check_even_or_odd(n):
#     ...
#     ...
#     return result

 #Output for an even numner
### $ Enter a number: 2
### $ 2 is an even number

#Output for a odd number
### $ Enter a number: 3
### $ 3 is a odd number








# print()

# add(51, 8)

# print(result)
