import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=400, height=600)
screen.bgcolor("black")
colors = ["green", "yellow", "blue", "red", "purple", "orange", "white"]
x_pos = (-130, -90, -50,  10,  50,  90, 130)

turtles = []

# -120, -80, -40,  0,  40,  80, 120

# Create 6 turtles
for i in range(7):
    new = Turtle(shape="turtle")
    new.setheading(90)
    new.color(colors[i])
    new.penup()
    new.goto(x_pos[i], -250)

    turtles.append(new)

# print(turtles)


response = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?").lower()

if response not in colors:
    print("Invalid")

# # Let's make the turtles run...
is_racing = True
while is_racing:
    for turtle in turtles:
        turtle.speed(1)
        turtle.forward(random.randint(1, 20))
        if turtle.ycor() > 250:
            if response == turtle.color()[0]:
                print(f"You've won!.. The winner id {turtle.color()[0]}")
                is_racing = False
            else:
                print("You lose! :(")
                is_racing = False


screen.mainloop()
