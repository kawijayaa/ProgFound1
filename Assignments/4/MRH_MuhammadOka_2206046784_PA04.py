##
## Programming Assignment 4 : Finale
## EAN-13 Barcode Generator
## by Muhammad Oka - 2206046784
##

from tkinter import *
from tkinter.messagebox import showerror
from random import randint

class Barcode:
    def __init__(self):
        """
        Initialize basic tkinter structures to run the program.
        """

        # Create tkinter window
        window = Tk()

        # Change window title
        window.title("EAN-13 Barcode Generator")
        
        # Create frame for labels and entries
        frame = Frame(window)
        frame.pack()

        # Create entries and labels
        save_label = Label(frame, text="Save barcode to PS file (eg: Test.eps):", font=("Arial", 16))
        self.filename = Entry(frame, width=50)
        code_label = Label(frame, text="Enter code (first 12 digits):", font=("Arial", 16))
        self.code = Entry(frame, width=50)

        # Add a event listener to the entries
        self.filename.bind("<Return>", self.parseFilename)
        self.code.bind("<Return>", self.parseCode)
        
        # Put the entries and labels to a grid system
        save_label.grid(row=0, padx=30, pady=(20, 0))
        self.filename.grid(row=1, padx=30, pady=5)
        code_label.grid(row=2, padx=30, pady=5)
        self.code.grid(row=3, padx=30, pady=(0, 15))

        # Create canvas for drawing the barcode
        self.canvas = Canvas(window, bg="white")
        self.canvas.pack(pady=(0, 20))

        # Run the window loop
        window.mainloop()
    
    def parseFilename(self, event):
        """
        To check if the file name entered is valid
        """

        # Get filename from entry
        inp = self.filename.get()

        # Check if filename ends in .eps
        if not inp.endswith(".eps"):
            # Tell the user that the file name is invalid
            showerror(title="Invalid input!", message="Invalid file name!")
        else:
            if self.code.get() != "": # Check if code entry is not empty
                # Parse the code
                self.parseCode(any) 

    def getEANStructure(self, first_digit: int):
        """
        Return the corresponding encoding structure of the first 6 digits
        """

        # Lookup table for the EAN-13 structure
        EANStructure = ["LLLLLL", "LLGLGG", "LLGGLG", "LLGGGL", "LGLLGG", "LGGLLG", "LGGGLL", "LGLGLG", "LGLGGL", "LGGLGL"]

        # Return the EAN-13 structure
        return EANStructure[first_digit]

    def encodeDigit(self, digit: int, code: str):
        """
        Encode the digit using the corresponding code
        """

        # Lookup table for R-code
        r_code = ["1110010", "1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100"]

        # If code is R
        if code == "R":
            # Return R-code
            return r_code[digit]
        # If code is G
        elif code == "G":
            # Return reversed R-code
            return r_code[digit][::-1]
        # If code is L
        elif code == "L":
            # Return xored R-code
            return "".join(["0" if x == "1" else "1" for x in r_code[digit]])

    def getCheckDigit(self, code: str):   
        """
        Calculate the check digit for an EAN-13 Barcode
        """     

        # Calculate for the even placed digits
        even = sum(int(x) for x in code[1::2]) 

        # Calculate for the odd placed digits
        odd = sum(int(x) for x in code[::2]) 
        
        # Calculate the checksum
        checksum = (even*3 + odd) % 10

        # Calculate the check digit, then return
        return checksum if checksum == 0 else 10-checksum 

    def parseCode(self, event):
        """
        Parse the input code for drawing
        """

        # Get the code from the entry
        code = self.code.get()

        # Check if code is only numbers or not
        if code.isdigit():
            # Check if the length of the digits is 12 or not
            if len(code) != 12:
                # Tell user that the code is invalid
                showerror(title="Invalid input!", message="Invalid code! Code must be 12 digits!")
            else:
                # Check if filename entry is not empty
                if self.filename.get() != "":
                    # Get check digit
                    checkDigit = self.getCheckDigit(self.code.get())

                    # Add the check digit at the back of the code
                    new_code = str(code) + str(checkDigit)

                    # Get the encoding structure for the first 6 digits
                    structure = self.getEANStructure(int(new_code[0]))

                    # Initialize list for the encoded code
                    code_encoded = []

                    # Iterate through the first 6 digits
                    for x in range(6): 
                        # Encode the digits using the structure from the first digit
                        code_encoded.append(self.encodeDigit(int(new_code[x + 1]), structure[x])) 
                    # Iterate through the last 6 digits
                    for x in range(6): 
                        # Encode the digits using the "R" encoding structure
                        code_encoded.append(self.encodeDigit(int(new_code[7 + x]), "R"))

                    # Generate the barcode
                    self.generateBarcode(new_code, code_encoded)

                    # Save the canvas to a file
                    self.canvas.postscript(file=self.filename.get())
                else:
                    # Tell the user that the file name is invalid
                    showerror(title="Invalid input!", message="Invalid file name!")
        else:
            # Tell the user that the code is invalid
            showerror(title="Invalid input!", message="Invalid code! Code must be numbers only!")

    def clamp(self, minimum, x, maximum):
        """
        Clamp a number to a minimum and a maximum
        """

        # Return the clamped number
        return max(minimum, min(x, maximum))

    def rgbToHex(self,r,g,b):
        """
        Convert rgb values to hex digit
        """

        # Return the converted values
        return f"#{r:02x}{g:02x}{b:02x}"

    def generateBarcode(self, code: str, code_list: list):
        """
        Add EAN-13 standard bars and draw the barcode to the canvas
        """

        # Clear the canvas
        self.canvas.delete("all")

        # Get the canvas width and height
        canvas_width = self.canvas.winfo_reqwidth()
        canvas_height = self.canvas.winfo_reqheight()

        # Add start, end, and guard bars
        code_list = ["101"] + code_list[:6] + ["01010"] + code_list[6:] + ["101"]

        # Convert the code list to a string
        code_list_draw = "".join(code_list)

        # Calculate the starting x and y position
        start_x = (canvas_width - (len(code_list_draw) * 2)) / 2
        start_y = (canvas_height - 110) / 2

        # Calculate check digit
        checkDigit = self.getCheckDigit(self.code.get())

        # Randomize color
        r, g, b = randint(0,63), randint(0,63), randint(0,63)

        # Iterate through the joined code
        for x in range(len(code_list_draw)):
            # Increase the red and green line color to make a rainbow effect
            color = self.rgbToHex(self.clamp(0, r + 2 * x, 200), self.clamp(0, g + 2 * x, 200), b)

            # Check if the current position is a start, end or a guard bar
            if x in [0, 1, 2, 45, 46, 47, 48, 49, 92, 93, 94]:
                if code_list_draw[x] == "1": # If the code is 1
                    # Draw a longer line for the start, end and guard bars
                    self.canvas.create_line(start_x + ((2 * x)), start_y, start_x + ((2 * x)), start_y + 110, fill=color, width=2)
            else:
                if code_list_draw[x] == "1": # If the code is 1
                    # Draw a line
                    self.canvas.create_line(start_x + ((2 * x)), start_y, start_x + ((2 * x)), start_y + 100, fill=color, width=2)

        # Draw the digits
        # Iterate through the normal code
        for x in range(len(code)):
            # If this is the first digit...
            if x == 0:
                # Draw the digits to the left of the start bar
                self.canvas.create_text(start_x - 7, start_y + 105, text=code[x])
            # If this is the first six digits (excluding the first digit)...
            elif x > 0 and x <= 6:
                # Draw the digits at the bottom of the linese
                self.canvas.create_text(start_x + (14 * x), start_y + 105, text=code[x])
            # If this is the last six digits...
            elif x > 6:
                # Draw the digis at the bottom of the lines
                self.canvas.create_text(start_x + 5 + (14 * x), start_y+105, text=code[x])

        # Draw text
        self.canvas.create_text(canvas_width / 2, start_y - 30, text="EAN-13 Barcode: ", font=("Arial", "16"), fill="black")

        # Draw the check digit
        self.canvas.create_text(canvas_width / 2, start_y + 140, text=f"Check Digit: {checkDigit}", font=("Arial", "16"), fill="red")

def main():
    # Create a new Barcode object
    program = Barcode()

if __name__ == "__main__":
    main()