####################
#   Assignment 2   #
#   Muhammad Oka   #
#    2206046784    #
####################

# Import required modules
import string
from htmlFunctions import *

# Print text
print("Program to create word clouds from a text file")
print()
print("The result is stored as an HTML file,")
print("which can be displayed in a web browser")
print()

filename = input("Please enter the file name: ") # Ask user for input

# Try to open file
try:
    txt = open(filename, "r")
except FileNotFoundError: # If file not found...
    print("File not found.")
    quit() # Stop the program

stop_word = open("stopWords.txt", "r").read().split("\n") # Read stop words text file and split by newline
punctuation = string.punctuation + "()" # Customizing the punctuation list by adding parentheses

txt_modified = txt.read().lower().replace("\n", " ") # Read the text file, make it lowercase, and removing the newlines
txt_modified = txt_modified.translate(str.maketrans(" ", " ", punctuation)) # Remove the punctuation
txt_list = txt_modified.split(" ") # Split the text file to a list
txt_filtered = [] # Initiate a variable for the filtered words

for word in txt_list: # Iterate through every word in the text file
    if word == "": # If the word is empty
        continue
    if word in stop_word: # If the word is a stop word
        continue
    else:
        txt_filtered.append(word) # Add the word to the filtered words list

word_count = [txt_filtered.count(word) for word in txt_filtered] # Count every word occurences in the text and put it in a list
word_frequencies = dict(zip(txt_filtered, word_count)) # Combine the words and their respective counts to a dictionary

# Sort the word frequencies from the highest frequency
sorted_word_frequencies = sorted(word_frequencies.items(), key=lambda t: t[::-1], reverse=True) # Use the frequencies to sort the tuples

# Print text
print(f"{filename} :")
print("60 words in frequency order as count:word pairs")
print()

first_sixty = sorted_word_frequencies[:60] # Find the first 60 words

for i in range(20): # Iterate through every row
    for j in range(3): # Iterate through every columns
        to_print = f"{first_sixty[3*i+j][1]:>3}:{first_sixty[3*i+j][0]}" # Format the word and count for primting
        print(f"{to_print:20s} ", end="") # Print the result
    print()

# Create word clouds HTML file

highest_count = first_sixty[0][1] # Get the highest count from the first tuple
lowest_count = first_sixty[59][1] # Get the lowest count from the last tuple
first_sixty.sort() # Re-sort the list alphabetically

body = ""

for i in range(20): # Iterate through every row
    for j in range(3): # Iterate through every column
        body += " " + make_HTML_word(first_sixty[3*i+j][0], first_sixty[3*i+j][1], highest_count, lowest_count) # Add the word to the HTML body

box = make_HTML_box(body)  # Creates HTML body
print_HTML_file(box, filename)  # Create HTML file

print()
input("Press the Enter key to exit...")