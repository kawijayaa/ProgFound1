kata_depan = ['dalam', 'atas', 'antara', 'kepada', 'akan', 'terhadap', 'oleh', 'dengan', 'berkat', 'tentang', 'sampai', 'guna', 'demi', 'untuk', 'bagi', 'menurut']

try:
    with open('input.txt', 'r') as f:
        count = 0
        file = f.read()
        file = file.replace("\n", " ").split(" ")

        for word in file:
            if word.lower() in kata_depan:
                count += 1
        
        print(count)
except FileNotFoundError:
    print('File not found')


def checkNPM(npm):
    a = 3 * (int(npm[0]) + int(npm[2]) + int(npm[4]) + int(npm[6]) + int(npm[8]))
    b = int(npm[1]) + int(npm[3]) + int(npm[5]) + int(npm[7])
    c = (a + b) % 7

    if int(npm[9]) == c:
        return (c, True)
    else:
        return (c, False)
    
l1 = [2,3,4]
l2 = l1
l3 = l1[:]

print(l3 is l1)
print(l3 == l1)
print(l3[0] is l1[0])
print(l2 == l1)
print(l2 is l1)

l = [12,20,-15,-7,-9]
l.sort(key=lambda x:abs(x), reverse=True)
print(l)

newList = []
c = "2020 Thomas Cup 2021"
i = 0
while i < len(c):
    if c[i].isdigit():
        newList.append(c[i])
    i += 1
print(newList)

def biner2desimal(binstr):
    noBits = len(binstr)
    temp = binstr
    newInt = 0
    for x in temp:
        if x == "1":
            newInt += 2**(len(temp)-1) * int(x)
            temp = temp[1:]
        else:
            temp = temp[1:]
    if binstr[0] == "1":
        newInt = (2**noBits - newInt) * -1
    return newInt

print(biner2desimal("10000000000"))