from turtle import *
from random import *

# Configure Turtle
t = Turtle()
t.speed(0)
t.hideturtle()

# Ask user for input
lowermost_bricks = int(numinput("Candi", "Enter the amount of bricks in the lowermost row: "))
uppermost_bricks = int(numinput("Candi", "Enter the amount of bricks in the uppermost row: "))
length = int(numinput("Candi", "Enter the length of the bricks: "))
width = int(numinput("Candi", "Enter the width of the bricks: "))

screen = getscreen()
screen.screensize(canvwidth=(length*uppermost_bricks+200), canvheight=(width*(lowermost_bricks-(uppermost_bricks-1))/2))

# Define brick drawing sequence
def draw_brick(l, w):
    for _ in range(2):
        t.fd(l)
        t.lt(90)
        t.fd(w)
        t.lt(90)

# Define variables for the loops
current_row = lowermost_bricks
num_of_bricks = 0

# Go to the starting position
t.up()
t.goto(-(length*lowermost_bricks)/2, -(width*(lowermost_bricks-(uppermost_bricks-1)))/2)
t.down()

# Draw candi
while current_row >= uppermost_bricks:
    for i in range(current_row): # If statement for color
        if current_row == lowermost_bricks or current_row == uppermost_bricks or i == 0 or i == current_row - 1:
            t.color("#AA4A44")
        else:
            t.color(random(), random(), random())
        
        # Draw the bricks
        t.begin_fill()
        draw_brick(length, width)
        t.end_fill()

        # Go to the next position for the next brick
        t.up()
        t.goto(t.xcor()+length, t.ycor())
        t.down()
    num_of_bricks += current_row # Add the number of bricks for the text
    current_row -= 1

    # Go to next row
    t.up()
    t.goto(-(length*current_row)/2, t.ycor()+width)
    t.down()

# Go below the candi to write text
t.up()
t.goto(0, (-(width*(lowermost_bricks-(uppermost_bricks-1)))/2)-50)
t.down()

# Write text
t.color("black")
t.write(f"Candi with {num_of_bricks} bricks", align="center", font=("Arial", 18, "normal"))

exitonclick()