######################################
# Author : Muhammad Oka - 2206046784 #
# File name : lab02b.py              #
# Using turtle to draw regular       #
######################################

# Importing turtle module
import turtle

# Initialize turtle module
turtle.shape("turtle")
turtle.title("Lab 02")

# Ask for the number of sides
sides = turtle.numinput("Lab 02", "Enter number of sides: ")

# Calculating length using formula 400/n
length = int(400 / int(sides))

# Moving the cursor
turtle.up()
turtle.goto(0,150)
turtle.down()

# Draw polygon (outline only)
for _ in range(int(sides)):
    turtle.fd(length)
    turtle.rt(360/sides)

# Ask for color in rgb format
red = turtle.numinput("Lab 02", "Enter red color (0-1): ")
green = turtle.numinput("Lab 02", "Enter green color (0-1): ")
blue = turtle.numinput("Lab 02", "Enter blue color (0-1): ")

# Moving the cursor down to make space
turtle.up()
turtle.goto(0,-150)
turtle.down()

# Create polygon with color
turtle.begin_fill()
for _ in range(int(sides)):
    turtle.color(red,green,blue)
    turtle.fd(length)
    turtle.rt(360/sides)
turtle.end_fill()

# Hide turtle
turtle.hideturtle()
# Message for user
print("Please click on the graphics windows to exit...")
# Wait for click to exit
turtle.exitonclick()