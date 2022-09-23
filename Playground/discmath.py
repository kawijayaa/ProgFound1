def implies(p, q):
    return not(p) or q

def biconditional(p,q):
    return ((not p) or q) and ((not q) or p) 

def logical_xor(p,q):
    return bool(p) ^ bool(q)

formula1, formula2, formula3 = True, True, True

for i in range(16):
    truth_value = format(i, '04b')
    p,q,r,s = bool(int(truth_value[0])), bool(int(truth_value[1])), bool(int(truth_value[2])), bool(int(truth_value[3]))
    formulaa1 = (r and (implies(p, q))) or (implies(not(q),r))
    formulaa2 = biconditional(implies(not(r), p), (biconditional(p, q) and r))
    formulab1 = implies(p,s) or (r and r or p and not(q)) and implies(q, r)
    formulab2 = not(p) or not(q) or r or s
    formulac1 = biconditional(not(p), r) and implies(q, p) and implies(r, not(p))
    formulac2 = not(p) and r or p and not(r)
    
    if formulaa1 == formulaa2:
        if formula1:
            formula1 = True
        else:
            formula1 = False
    else:
        formula1 = False

    if formulab1 == formulab2:
        if formula2:
            formula2 = True
        else:
            formula2 = False
    else:
        formula2 = False

    if formulac1 == formulac2:
        if formula3:
            formula3 = True
        else:
            formula3 = False
    else:
        formula3 = False

if formula1:
    print("Question A is Equivalent")
else:
    print("Question A is Not Equivalent")

if formula2:
    print("Question B is Equivalent")
else:
    print("Question B is Not Equivalent")

if formula3:
    print("Question C is Equivalent")
else:
    print("Question C is Not Equivalent")