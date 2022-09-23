print('Lab 03 -- 2022\n')
print('From decimal to octal')
print('----------------------')
# read the user's input
myInt = int(input("Give a positive integer in decimal representation: "))

# convert the integer given by the user stored in myInt to a octal representation
octstr = ''                       # accumulator for binary digits, start with empty string
temp = myInt

while temp > 0:
    octdigit = temp
    octstr = octstr + str(octdigit % 8)
    temp = octdigit // 8 

print(f"The octal representation of {myInt} is 0o{octstr[::-1]}")
print()
print('From octal to decimal')
print('----------------------')

# read the octal string from the user's input

octstr = input('Give a positive integer in octal representation: ')
# convert the octal string to a correct decimal integer
temp = octstr[2:]         # remove '0o' using string slicing
newInt = 0
length = len(temp)
for i in range(0, length):
    octdigitstr = temp[-1:]              # get the rightmost octal digit
    octdigit = int(octdigitstr)
    newInt += octdigit * 8** i   # add the appropriate power
    temp = temp[:-1]                     # remove the rightmost octal digit
print(f"The decimal representation of {octstr} is {newInt}")
print()
print('Thank you for using this program.')
print()
input('Press Enter to continue ...')