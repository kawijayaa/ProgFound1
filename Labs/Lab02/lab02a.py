import turtle

turtle.color("green") # Set pen color to green

# Draw polygon
for _ in range(6):
    turtle.fd(100)
    turtle.rt(360/6)

turtle.hideturtle() # Hide the turtle
turtle.exitonclick() # Wait for click to exit