from time import sleep
import turtle as t

t.tracer(1, 0) # Increase the first argument to speed up the drawing
t.setworldcoordinates(0, 0, 700, 700)
t.color("blue")
t.hideturtle()

LINE_LENGTH = 8
ANGLE = 90
LEVELS = 5

def hilbertCurveQuadrant(level, angle):
    if level == 0:
        pass
    else:
        t.right(angle)
        hilbertCurveQuadrant(level-1, -angle)
        t.forward(LINE_LENGTH)
        t.left(angle)
        hilbertCurveQuadrant(level-1, angle)
        t.forward(LINE_LENGTH)
        hilbertCurveQuadrant(level-1, angle)
        t.left(angle)
        t.forward(LINE_LENGTH)
        hilbertCurveQuadrant(level-1, -angle)
        t.right(angle)
        return

def hilbertCurve(startPos):
    t.penup()
    t.goto(startPos)
    t.pendown()

    hilbertCurveQuadrant(LEVELS, ANGLE) # Draw lower left quadrant
    t.forward(LINE_LENGTH)

    hilbertCurveQuadrant(LEVELS, ANGLE) # Draw lower right quadrant
    t.left(ANGLE)
    t.forward(LINE_LENGTH)
    t.left(ANGLE)

    hilbertCurveQuadrant(LEVELS, ANGLE) # Draw upper right quadrant
    t.forward(LINE_LENGTH)

    hilbertCurveQuadrant(LEVELS, ANGLE) # Draw upper left quadrant

    t.left(ANGLE)
    t.forward(LINE_LENGTH)
    t.left(ANGLE)

t.title("A Hilbert Curve Fractal")
hilbertCurve((30, 350))
t.exitonclick()