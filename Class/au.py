count = 0
for i in range(3):
    for j in range(1, 4):
        count += i*j

count2 = 0
for i in range(3):
    for j in range(4):
        count2 += (2*i) + (3*j)

print(count)
print(count2)