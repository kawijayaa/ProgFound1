# ( )()()()()()()()()()()()()()( )
#  |                            |
#  |  Programming Assignment 1  |
#  |  Muhammad Oka  2206046784  |
#  |                            |
# ( )()()()()()()()()()()()()()( )

# Import modules
from turtle import *
from random import randint

# Initialize screen and turtle
screen = getscreen()
turtle = Turtle()

# Configure turtle
title("Colorful Chessboard and Flower")
colormode(255)
turtle.speed(0)
turtle.hideturtle()

# Ask for input
rows = numinput("Colorful Chessboard and Flower", "Enter number of rows: ", minval=2, maxval=25)
square_size = numinput("Colorful Chessboard and Flower", "Enter square size (pixels): ")
petals = numinput("Colorful Chessboard and Flower", "Enter number of petals: ", minval=2, maxval=25)

# Define square and petal function so we dont have any repetitive code
def square():
    turtle.fillcolor(randint(0,255), randint(0,255), randint(0,255)) # Random colors
    turtle.begin_fill()
    for _ in range(4): # Create a square
        turtle.fd(square_size)
        turtle.lt(90)
    turtle.end_fill()

def petal():
    turtle.fillcolor(randint(0,255), randint(0,255), randint(0,255)) # Random colors
    turtle.begin_fill()
    turtle.circle(50,90)
    turtle.right(-90)
    turtle.circle(50,90)
    turtle.end_fill()

# Create chessboard
# Go to starting position
turtle.up()
turtle.goto(-(square_size*rows)/2,-50) # This is needed for making the chessboard center to the screen
turtle.down()
# Loop rows
for i in range(1, int(rows)+1):
    # Loop columns
    for _ in range(int(rows)):
        turtle.down()
        square()
        up()
        turtle.fd(square_size)
        turtle.down()
    # Move to next row
    turtle.up()
    turtle.goto(-(square_size*rows)/2, turtle.ycor() - square_size)
    turtle.down()

# Create flower
# Go to starting position
turtle.up()
turtle.goto(0,150)
turtle.down()
# Create petals
for x in range(1, int(petals)+1):
    petal()
    turtle.setheading(360*(x/petals)) # Rotate evenly to create next petal

# Create text
turtle.up()
turtle.goto(0, -250)
turtle.down()
turtle.write(f"Colorful Chessboard of {int(rows**2)} squares and Flower {int(petals)} petals.", align="center", font=("Arial", 24, "normal"))

# Exit on click
exitonclick()