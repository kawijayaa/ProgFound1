##################
##    Lab 03    ##
## Muhammad Oka ##
##  2206046784  ##
##################

print("Lab 03 -- 2022")
print()
print("From Decimal to Octal")
print("---------------------")

# Ask for input
dec_input = int(input("Give a positive integer in decimal representation: "))

# Initialize quotient and remainder string
quotient = dec_input
remainders = ""

# Calculate octal representation
while quotient > 0:
    remainders += str(quotient % 8) # Save the remainder to a string
    quotient = quotient // 8 # Get the quotient 

# [::-1] is used to reverse the remainder string, since we need to read it backwards
print(f"The octal representation of {dec_input} is 0o{remainders[::-1]}.")

print("From Octal to Decimal")
print("---------------------")

# Ask for input
oct_input = input("Give a positive integer in octal representation: ")

oct_cleaned = oct_input[2:] # Remove the "0c" prefix
oct_cleaned = oct_cleaned[::-1] # Reverse the input so we can start from the least significant digit
oct_final = 0

# Calculate decimal by weight
for i in range(len(oct_cleaned)):
    oct_final += int(oct_cleaned[i]) * (8**i) # (i)th input x 8^i

print(f"The decimal representation of {oct_input} is {oct_final}.")

print()

print("Thank you for using this program.")
input("Press Enter to continue...")