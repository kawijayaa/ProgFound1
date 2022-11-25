from tkinter import *
from tkinter.colorchooser import askcolor

class Scribbler(object):
    def __init__(self):
        # Create window
        window = Tk()
        window.title("Scribbler")

        # Initialize variables for drawing
        self.prev_x, self.prev_y = 0, 0
        self.color = "green"

        # Create canvas
        self.canvas = Canvas(window, bg="white", width=400, height=250)
        # To detect mouse button click and motion
        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)
        # Pack the canvas
        self.canvas.pack(expand=True, fill=BOTH)

        # Create frame for storing buttons and labels
        frame = Frame(window)
        frame.pack(side=TOP)

        # Create buttons and label
        self.clear_button = Button(frame, bg="orange", text="Clear", command=self.clear)
        self.color_button = Button(frame, bg=self.color, text="Color", command=self.change_color)
        self.label = Label(window, text="Press and drag the left mouse button to draw", fg="blue")

        # Pack buttons and labels
        self.clear_button.pack(side=LEFT, padx=5)
        self.color_button.pack(side=LEFT)
        self.label.pack(side=BOTTOM)

        # Run the window loop
        window.mainloop()

    def begin(self, event): # When left mouse button is clicked
        # Set current mouse x, y coordinate as previous x, y
        self.prev_x = event.x
        self.prev_y = event.y
    
    def draw(self, event): # When left mouse button is clicked and mouse is moved
        # Get current mouse x, y coordinate
        current_x = event.x
        current_y = event.y

        # Create a line from the previous x, y to the current x, y
        self.canvas.create_line(self.prev_x, self.prev_y, current_x, current_y, fill=self.color)

        # Set current mouse x, y coordinate as previous x, y
        self.prev_x = current_x
        self.prev_y = current_y

    def clear(self):
        # Clear the canvas
        self.canvas.delete("all")

    def change_color(self):
        # Ask user for color from color picker
        self.color = askcolor()[-1]
        # Set the color to the color button
        self.color_button["bg"] = self.color

if __name__ == "__main__":
    Scribbler() # Create new Scribbler object