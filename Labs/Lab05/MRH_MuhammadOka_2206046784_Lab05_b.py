def putNumber(num, string): # Create new function
    # Use :03d to add leading zeros that makes the length of the integer to 3
    return (f"{num:03d}. {string}") # Return the formatted string

def main(): # Main function
    input_filename = input("Enter the name of your input text file: ") # Ask user for input file name
    try:
        txt = open(input_filename, "r").read() # Read the input file
    except FileNotFoundError: # If the input file not found
        print("File not found!")
        quit()
    output_filename = input("Enter the name of your output text file: ") # Ask user for output file name
    txt_out = open(output_filename, "w") # Create a new txt file for output
    txt_lines = txt.split("\n") # Split the text on a newline character
    total_char = 0 # Initialize variable for counting the total characters of the input file

    for i in range(len(txt_lines)): # Iterate through every line
        txt_out.write(putNumber(i+1, txt_lines[i]) + "\n") # Write to output file
        total_char += len(txt_lines[i]) # Add the length of current line to the total of characters
    txt_out.write(f"\nThe total number of characters of input is: {total_char}") # Write the total characters to output file
    print(f"\nThe total number of characters of input is: {total_char}") # Print the total characters of input
    txt_out.close()

if __name__ == "__main__": # If we run this file...
    main() # Call the main function