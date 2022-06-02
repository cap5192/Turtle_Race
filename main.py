from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500, height = 400)
choice = screen.textinput(title = "Make your bet", prompt = "Make your bet, which color of the turtle will win?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tim = Turtle(shape="turtle")


screen.exitonclick()