"""
Lab 10 FPROG1 2022
- draw elastic (rubber) shapes on a canvas by
a left mouse-click and dragging,
- move the last drawn shape by a right mouse-click
"""
from tkinter import *
from tkinter.colorchooser import askcolor
class DrawRubberShapes(object):
    # Construct the GUI
    def __init__(self):
        window = Tk() # Create a window
        window.title("Lab 10: Drawing Rubber Shapes") # Set a title
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()

        # Create a button for choosing color using a color chooser
        self.fillColor = StringVar()
        self.fillColor.set('red')
        def colorCommand():
            (rgb,color) = askcolor()
            if color != None:
                self.fillColor.set(color)
                colorButton["bg"] = color
        colorButton = Button(frame1, text = "Color", command=colorCommand, bg = self.fillColor.get())
        colorButton.grid(row=1,column=1,columnspan=2)
        clearButton = Button(frame1, text = "Clear", command=self.clear, bg = "cyan")
        clearButton.grid(row=1,column=6,columnspan=2)

        # Create radio buttons for geometrical shapes
        self.v1 = StringVar(value="R")
        rbRectangle = Radiobutton(frame1, text = "Rectangle", variable = self.v1, value = 'R', command = self.processRadiobutton)
        rbLine = Radiobutton(frame1, text = "Line", variable = self.v1, value = 'L', command = self.processRadiobutton)
        rbOval = Radiobutton(frame1, text = "Oval", variable = self.v1, value = 'O', command = self.processRadiobutton)
        rbRectangle.grid(row = 1, column = 3)
        rbLine.grid(row = 1, column = 4)
        rbOval.grid(row = 1, column = 5)

        # Create a canvas, bound to mouse events
        canvas = Canvas(window, width=400, height=300)
        self.canvas = canvas
        self.canvas.pack()
        self.canvas.bind('<ButtonPress-1>', self.onStart) # left click
        self.canvas.bind('<B1-Motion>', self.onGrow) # drag
        self.canvas.bind('<ButtonPress-3>', self.onMove) # right click

        # for remembering the last drawing
        self.drawn = None
        self.shape = self.canvas.create_rectangle

        window.mainloop()

    def processRadiobutton(self):
        # Check which radio button is selected
        if self.v1.get() == "R":
            self.shape = self.canvas.create_rectangle
        elif self.v1.get() == "L":
            self.shape = self.canvas.create_line
        elif self.v1.get() == "O":
            self.shape = self.canvas.create_oval

    def onStart(self, event):
        self.start = event
        self.drawn = None

    # elastic drawing: delete and redraw, repeatedly
    def onGrow(self, event):
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x,
        event.y, fill=self.fillColor.get())
        self.drawn = objectId
        
    # move the shape to the click spot
    def onMove(self, event):
        if self.drawn:
            canvas = event.widget

            # Get current position of shape
            x0, y0, x1, y1 = canvas.coords(self.drawn)

            # Calculate width and height
            width = x1 - x0
            height = y1 - y0
            
            diffX, diffY = (event.x-(x0+(width/2))),(event.y-(y0+(height/2)))
            canvas.move(self.drawn, diffX, diffY)
            self.start = event
    
    # to clear the canvas on button click
    def clear(self):
        self.canvas.delete("all")

if __name__ == '__main__':
    DrawRubberShapes()