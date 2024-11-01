# need to install tkinter
import turtle

# turtle is a module
# Turtle is a class

# create an object
timmy = turtle.Turtle()

# also you can use
# from turtle import Turtle
# timmy = Turtle()

print(timmy)

# set the shape to turtle
timmy.shape("turtle")

# set the pen color to red, fill color to green
timmy.color("red", "green")

# make the object forward 100 steps/pixels
timmy.forward(100)

# add screen object
my_screen = turtle.Screen()
# print(my_screen.canvheight)

# make the screen exit on click
my_screen.exitonclick()