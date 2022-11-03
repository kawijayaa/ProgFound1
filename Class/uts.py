def div2(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count

def checksumNPM(npm):
    a = 3 * (int(npm[0]) + int(npm[2]) + int(npm[4]) + int(npm[6]) + int(npm[8]))
    b = int(npm[1]) + int(npm[3]) + int(npm[5]) + int(npm[7])
    c = (a + b) % 7
    return c



# print(checksumNPM("2206823291"))+
print((22*3 + 12) % 7)