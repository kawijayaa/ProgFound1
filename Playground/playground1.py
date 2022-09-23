inp = input("Enter binary to complement: ")
x = int(inp,2) ^ int("1"*len(inp),2)
out = bin(x+1)[2:]
out = out[-len(inp):]
if len(out) < len(inp):
    out = "0"*(len(inp)-len(out)) + out
if inp[0] == "0":
    print(f"{len(inp)} bit Number \nINPUT = {inp} | {int(inp,2)} \nOUTPUT = {out} | -{int(inp,2)}")
elif inp[0] == "1":
    print(f"{len(inp)} bit Number \nINPUT = {inp} | -{int(out,2)} \nOUTPUT = {out} | {int(out,2)}")