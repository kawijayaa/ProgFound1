def rev(L):
    if L == []:
        return L
    return [L[-1]] + rev(L[:-1])

print(rev([1,2,3,4]))