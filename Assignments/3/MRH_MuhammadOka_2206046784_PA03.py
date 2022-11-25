# ================================= #
# =   Programming Assignment 03   = #
# =        The Maze Runner        = #
# =               by              = #
# =   Muhammad Oka - 2206046784   = #
# ================================= #

import random
from tkinter import *

class MazeRunner:
    def __init__(self):
        self.window = Tk() # Create new window
        self.window.title("Maze Runner") # Set window title

        frame = Frame(self.window, width=500, height=500) # Create new frame
        frame.pack() # Pack frame for rendering

        size_label = Label(frame, text="Enter your maze size: ") # Create label for textbox
        self.size = Entry(frame) # Create textbox
        randomize_maze = Button(frame, text="Randomize Maze", command=self.create_maze) # Create button for randomizing maze
        find_route = Button(frame, text="Find Escape Route", command=self.solve_maze) # Create button for finding solution

        # Put label, textbox and buttons in a grid
        size_label.grid(row=0, column=0, padx=2) 
        self.size.grid(row=0, column=1, padx=2)
        randomize_maze.grid(row=0, column=2, padx=2)
        find_route.grid(row=1, column=1, pady=2)

        self.canvas = Canvas(self.window, bg="white") # Create new canvas for maze
        self.canvas.pack() # Pack canvas for rendering
        self.window.mainloop() # Render window

    def create_maze(self):
        self.canvas.delete("all") # Clear the canvas

        self.width = self.canvas.winfo_reqwidth() # Get canvas width
        self.height = self.canvas.winfo_reqheight() # Get canvas height
        self.maze_size = int(self.size.get()) # Get maze size from textbox
        self.SQUARE_SIZE = 25 if self.maze_size < 10 else 175/self.maze_size # Set square size
        self.maze = [[random.randint(0,1) for j in range(int(self.maze_size))] for i in range(int(self.maze_size))] # Create maze matrix and randomize the contents
        self.solution = [[0 for j in range(int(self.maze_size))] for i in range(int(self.maze_size))] # Create zero matrix for the solution
        self.maze[0][0] = 1 # Set the top left box as a valid box (not a wall)

        start_x = (self.width/2) - ((self.SQUARE_SIZE*self.maze_size)/2) # Calculate starting x position for rendering maze
        start_y = (self.height/2) - ((self.SQUARE_SIZE*self.maze_size)/2) # Calculate starting y position for rendering maze

        for i in range(len(self.maze)): # Iterate through the rows of the maze matrix
            for j in range(len(self.maze[i])): # Iterate through the columns of the maze matrix
                if (i == 0 and j == 0) or (i == self.maze_size-1 and j == self.maze_size-1): # If current box is the top-left (start) or the-bottom right (end)
                    fill_color = "green" # Set color to green
                else:
                    if self.maze[i][j] == 1: # If the box is marked 1 (valid box)
                        fill_color = "white" # Set color to white
                    else: # If the box is marked 0 (a wall)
                        fill_color = "grey" # Set color to grey
                self.canvas.create_rectangle((j * self.SQUARE_SIZE) + start_x, (i * self.SQUARE_SIZE) + start_y, ((j + 1) * self.SQUARE_SIZE) + start_x, ((i + 1) * self.SQUARE_SIZE) + start_y, fill=fill_color) # Render a box

    def is_safe(self, maze, x, y, maze_size): 
        if (x >= 0 and x < maze_size) and (y >= 0 and y < maze_size) and maze[y][x]: # Check if x and y is out of bounds or not
            return True
        return False

    def recursive_solve(self, maze, x, y, maze_size):
        if x == maze_size - 1 and y == maze_size - 1: # Base case
            return True
        if self.is_safe(maze, x, y, maze_size): # If current x and y is safe (not out of bounds)
            if maze[y][x] == 0: # If current position is a wall
                return False
            else:
                self.solution[y][x] = 1 # Set current position as a valid solution
                if self.recursive_solve(maze, x+1, y, maze_size): # Move in x direction
                    return True
                if self.recursive_solve(maze, x, y+1, maze_size): # If x doesnt work, move in y direction
                    return True
                self.solution[y][x] = 0 # Else, set current position as an invalid solution
        return False

    def solve_maze(self):
        start_x = (self.width/2) - ((self.SQUARE_SIZE*self.maze_size)/2) # Calculate starting x position for rendering solution
        start_y = (self.height/2) - ((self.SQUARE_SIZE*self.maze_size)/2) # Calculate starting y position for rendering solution

        if self.recursive_solve(self.maze, 0, 0, self.maze_size) == False: # If we cannot find a solution
            # Render a text
            self.canvas.create_text(self.width/2, (self.height/2)+((self.SQUARE_SIZE*self.maze_size)/2)+20, text="Solution does not exist.", font=("Arial 15"), fill="black")

        for i in range(len(self.solution)): # Iterate through the rows of the solution matrix
            for j in range(len(self.solution[i])): # Iterate through the columns of the solution matrix
                if (i == 0 and j == 0) or (i == self.maze_size-1 and j == self.maze_size-1): # If the current box is the top-left (start) or the bottom-right (end)
                    fill_color = "green" # Set the color to green
                else:
                    if self.solution[i][j] == 1: # If the current box is marked 1 (A solution)
                        fill_color = "green" # Set the color to green
                    else: # If the current box is not a solution
                        fill_color = "" # Set the color to nothing
                if fill_color != "": # If fill color has a value
                    # Render the solution box
                    self.canvas.create_rectangle((j * self.SQUARE_SIZE) + start_x, (i * self.SQUARE_SIZE) + start_y, ((j + 1) * self.SQUARE_SIZE) + start_x, ((i + 1) * self.SQUARE_SIZE) + start_y, fill=fill_color)

# Create new object
maze = MazeRunner()