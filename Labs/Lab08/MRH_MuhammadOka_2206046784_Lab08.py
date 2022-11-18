#
# Lab08
# Muhammad Oka - 2206046784
#

import string

def substitute(char, dict): # To return the value from a key
    return dict[char]

def encrypt(secret, plain, charset): # Encrypt the Vigenere Cipher
    out = "" # Init output string
    for c in range(len(plain)): # Iterate through the plain text
        # Create lookup table for the substitution
        encrypt_dict = dict(zip(charset, charset[charset.index(secret[c % len(secret)]):] + charset[:charset.index(secret[c % len(secret)])])) 

        if plain[c] in charset: # If current character is in the character set
            out += substitute(plain[c], encrypt_dict) # Substitute character using the table and add it to the output variable
        else:
            out += plain[c] # Add the character as is to the output variable
    return out # Return the output string

def decrypt(secret, cipher, charset): # Decrypt the Vigenere Cipher
    out = "" # Init output string
    for c in range(len(cipher)): # Iterate through the cipher text
        # Create lookup table for the substitution
        encrypt_dict = dict(zip(charset[charset.index(secret[c % len(secret)]):] + charset[:charset.index(secret[c % len(secret)])], charset))

        if cipher[c] in charset: # If current character is in the character set
            out += substitute(cipher[c], encrypt_dict) # Substitute character using the table and add it to the output variable
        else:
            out += cipher[c] # Add the character as is to the output variable
    return out # Return the output string

def main(): # Main function
    # Ask user for inputs
    secret = input("Enter the secret keyword: ")
    input_filename = input("Enter the input file name: ")
    output_filename = input("Enter the output file name: ")
    method = input("(E)ncrypt or (D)ecrypt?: ")

    alphas = string.ascii_letters # Define the character set as all lowercase and uppercase letters

    with open(input_filename) as inp: # Open input filename
        inp = inp.read() # Read the input filename

    with open(output_filename, "w") as out: # Open output filename
        if method.upper() == "E": # If we are encrypting...
            out.write(encrypt(secret, inp, alphas)) # Write the output cipher text to the output file
        elif method.upper() == "D": # If we are decrypting...
            out.write(decrypt(secret, inp, alphas)) # Write the output plain text to the output file
    print(f"File saved to {output_filename}.")

if __name__ == "__main__":
    main()
