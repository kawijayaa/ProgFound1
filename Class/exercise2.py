from random import randint

length = int(input("Enter length of array: "))
num_array = []
max_buffer = 0
min_buffer = 10000

for i in range(length):
    num = randint(0, 10000)
    if num >= max_buffer:
        max_buffer = num
    if num <= min_buffer:
        min_buffer = num
    num_array.append(str(num))

print(f"{', '.join(num_array)} \n\nLargest number is {max_buffer}\nSmallest number is {min_buffer}")