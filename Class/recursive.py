from timeit import *

def balik(n):
    if n > 0:
        print(n%10)
        balik(n//10)

# balik(3124)

def cetak(n):
    if n > 0:
        cetak(n//10)
        print(n%10)

# cetak(31245)

def numOnes(n):
    if n == 0:
        return 0
    else:
        return n%2 + numOnes(n//2)
    
# print(numOnes(32))

dictio = {"a":36, "c":25, "b":40}

# print(dictio.keys())
# print(dictio.values())
# print(dictio.items())
# print(sorted(dictio.items()))
# print(sorted(dictio.items(), key=lambda x:x[::-1]))

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

# print(fib(3))

def palindrome(s):
    if len(s) < 2:
        return True
    
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False

# print(palindrome("racecar"))

def countneg(L):
    if L == []:
        return 0
        
    if L[0] < 0:
        return 1 + countneg(L[1:])
    else:
        return countneg(L[1:])

# print(countneg([23,7,9]))

def total(L):
    if L == []:
        return 0
    return L[0] + total(L[1:])

# print(total([-3,5,3,1]))

def reverseList(L):
    if L == []:
        return []
    return [L[-1]] + reverseList(L[:-1])

# print(reverseList([9, -3, 2, 0, 5, -12]))

def countDigit(st):
    if st == "":
        return 0
    return int(st[0].isdigit()) + countDigit(st[1:])
    # return ("0" <= st[0] <= "9") + countDigit(st[1:])

# print(countDigit("Year 2022"))

countDigit_recursion = """
def countDigit(st):
    if st == "":
        return 0
    return int(st[0].isdigit()) + countDigit(st[1:])
    # return ("0" <= st[0] <= "9") + countDigit(st[1:])
countDigit("Year 2022")
"""

countDigit2_iteration = """
def countDigit2(st):
    counter = 0
    for elem in st:
        if "0" <= elem <= "9":
            counter += 1
    return counter
countDigit2("Year 2022")
"""

# To know which is faster, recursion or iteration
# print(f"Recursion Time {timeit(stmt = countDigit_recursion):.2f}s")
# print(f"Iteration Time {timeit(stmt = countDigit2_iteration):.2f}s")

def perm(str):
    out_list = []
    out = ""
    if len(str) == 1:
        return str
    for i in str:
        out_list.append([i, perm(str.replace(i, ""))])
    for j in out_list:
        if type(j) is str:
            out += j
        else:
            out += "".join(j)
    return out

    
print(perm("abcd"))