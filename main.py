from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
choice = screen.textinput(title = "Make your bet", prompt = "Make your bet, which color of the turtle will win?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
random.shuffle(colors)
turtles = []
x = -230
y = -100
is_race = False
for i in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x, y)
    y += 50
    turtles.append(tim)
print(turtles)

if choice:
    is_race_on = True

while is_race_on:
    for i in turtles:
        rand_distance = random.randint(0, 10)
        if i.xcor() >= 230:
            is_race_on = False
            print(f"User chose {choice}.")
            print(f"Winner is: {tim.pencolor()}")
            if choice == tim.pencolor():
                print("You won!!")
            else:
                print("Sorry, but you lose bro")
        i.forward(rand_distance)
screen.exitonclick()