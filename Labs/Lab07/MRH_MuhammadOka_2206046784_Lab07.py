###############################
## -------- Lab 07 --------- ##
## Muhammad Oka - 2206046784 ##
###############################

def selectionSort(values:list):
    swaps = 0 # To track how many swaps we did
    for step in range(len(values)):
        min_index = step # Set the minimum element index to the step
        for i in range(step + 1, len(values)): # Iterate through every element after the step
            if values[i] < values[min_index]: # If the current element is smaller than the minimum
                min_index = i # Make the current element our new minimum
        values[step], values[min_index] = values[min_index], values[step] # Swap the elements
        if step != min_index: # To check if we did a swap or not
            swaps += 1 
    return swaps # Return the number of swaps


def main():
    inp = input("Enter a sequence of numbers (separate with commas): \n") # Ask user for input

    inp = inp.split(",") # Remove commas
    inp = [int(x.strip()) for x in inp] # Remove any whitespaces and convert elements to int
    print(f"Input list: \n{inp}") # Print input list

    num_of_swaps = selectionSort(inp) # Sort the list, and keep the return value (swaps)

    print(f"Sorted list: \n{inp}") # Print sorted list
    print(f"Number of swaps: {num_of_swaps}") # Print how many swaps we did

if __name__ == "__main__":
    main()