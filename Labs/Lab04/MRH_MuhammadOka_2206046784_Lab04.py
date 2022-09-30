import string
from math import ceil
from stop_words import get_stop_words

# The text we are analyzing
text = """The birds have left their trees
The light pours onto me
I can feel you lying there all on your own
We got here the hard way
All those words that we exchange
Is it any wonder things get broke?
'Cause in my heart and in my head
I'll never take back the things I said
So high above, I feel it coming down
She said, in my heart and in my head
Tell me why this has to end
Oh, no, oh, no
I can't save us, my Atlantis, we fall
We built this town on shaky ground
I can't save us, my Atlantis, oh, no
We built it up to pull it down
Now all the birds have fled
The hurt just leaves me scared
Losing everything I've ever known
It's all become too much
Maybe I'm not built for love
If I knew that I could reach you, I would go
It's in my heart and in my head
You can't take back the things you said
So high above, I feel it coming down
She said, in my heart and in my head
Tell me why this has to end
Oh, no, oh, no
I can't save us, my Atlantis, we fall
We built this town on shaky ground
I can't save us, my Atlantis, oh, no
We built it up to pull it down
Yeah, we build it up and we build it up
Yeah, we build it up to pull it down
And we build it up and we build it up
And we build it up to pull it down
I can't save us, my Atlantis, we fall
We built this town on shaky ground
I can't save us, my Atlantis, oh, no
We built it up to pull it down
"""

text = text.replace('\n', ' ') # Remove new line
text_split = text.split(" ") # Split the string into a list

# Initialize variables
cleaned_words = []
repeated_words = []

# Iterate through every single word in the list
for words in text_split:
    words = words.strip(string.punctuation).lower() # Remove punctuation and make it lowercase
    if words == "": # Do not add if the variable is empty
        continue
    if words in get_stop_words("english"): # Do not add if the word is a stop word
        continue
    
    if words not in cleaned_words: # If this is true, this is the first encounter of the word
        cleaned_words.append(words)
    else:
        if words not in repeated_words: # If this is false, the word is already repeated
            repeated_words.append(words) # This is the first time the word is repeated, so add the word to the list of repeated words

# Sort the list alphabetically
cleaned_words.sort()
repeated_words.sort()

# Print the "tables"
print("The sorted (A-Z) repeated words are:")
repeated_words_rows = ceil(len(repeated_words)/5) # Get the number of rows
for i in range(repeated_words_rows): # The range I used is the number of rows if every row has 5 words
    if i != repeated_words_rows - 1: # If this is not the last row
        for j in range(5): # 5 words per row
            print(f"{repeated_words[5*i+j]:15s}", end="") # Print the words with spacing
    else:
        for j in range(len(repeated_words) - (5*i)): # 5 words per row
            print(f"{repeated_words[5*i+j]:15s}", end="") # Print the words with spacing
    print()

print()

cleaned_words_rows = ceil(len(cleaned_words)/5) # Get the number of rows
print("The sorted (A-Z) cleaned words are:")
for i in range(cleaned_words_rows): # The range I used is the number of rows if every row has 5 words
    if i != cleaned_words_rows - 1: # If this is not the last row
        for j in range(5): # 5 words per row
            print(f"{cleaned_words[5*i+j]:15s}", end="") # Print the words with spacing
    else:
        for j in range(len(cleaned_words) - (5*i)): # 5 words per row
            print(f"{cleaned_words[5*i+j]:15s}", end="") # Print the words with spacing
    print()