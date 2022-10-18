# 29
def lsdd(n):
    return n%10

# 30
def sumSquare(n):
    if n == 1:
        return 1
    return n**2 + sumSquare(n-1)

# 31
def nomor31():
    outFile = open("kontol.txt", "w")
    print(23, file=outFile)
    print(117, file=outFile)
    print(-15, file=outFile)
    outFile.close()
    inFile = open("kontol.txt", "r")
    var = 0
    for line in inFile:
        var += int(line.strip())
    print(var)

# 33
def nomor33():
    lst1 = ["satu", "dua", "tiga", "empat"]
    lst2 = [kata[::-2] for kata in lst1]
    print(lst2)
    print(lst1[1][:1])

    list1 = [30,20,10,0,[41,42]]
    list2 = list1
    list3 = list2[:]
    list1[0] = 1
    list2[1] = 2
    list3[2] = 3
    list3[-1][1] = 5
    print(list2)
    print(list3)

# 34
def syr(x):
    out = []
    while x != 1:
        out.append(x)
        if x%2==0:
            x //= 2
        else:
            x = 3*x+1
    out.append(1)
    return out

# 35
even_cubes = [x**3 for x in range(50) if x%2==0]

# 36
def sumDigit(n):
    split = [int(x) for x in str(n)]
    out = 0
    for x in split:
        out += x
    return out

# 37
def wordLenghts(lst):
    out = []
    for word in lst:
        to_append = [word, len(word)]
        if to_append not in out:
            out.append(to_append)
    return out

# 38
q = [2*i if i%2==0 else 5*i for i in range(1,11)]

for i in range(1,11):
    if i%2==0:
        2*i
    else:
        5*i

out = [5,4,15,8,25,12,35,16,45,20]

# 39
L = [5,-8,3,7,15,-9,4,2]
L = sorted(L, key=lambda x: abs(x), reverse=True)