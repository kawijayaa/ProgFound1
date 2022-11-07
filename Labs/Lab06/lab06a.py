## Lab 06 A

def wordsToDigit(L): # Translate words to digits
    if len(L) == 1: # Base case
        match L[0]: # Pattern match the word to a digit
            case "zero":
                return 0
            case "one":
                return 1
            case "two":
                return 2
            case "three":
                return 3
            case "four":
                return 4
            case "five":
                return 5
            case "six":
                return 6
            case "seven":
                return 7
            case "eight":
                return 8
            case "nine":
                return 9
            case _:
                raise Exception("Input not valid")
    else: # Recursive case
        return wordsToDigit([L[0]])*(10**(len(L)-1)) + wordsToDigit(L[1:])


def main():
    inp = input("Enter a sequence of words: ") # Ask user for input
    inp_split = inp.split(" ") # Split input by whitespace
    print(wordsToDigit(inp_split)) # Merge the list and print

if __name__ == "__main__":
    main()