from time import sleep
from random import randint
import os

inp = input()
os.system("cls")
while True:
    for x in range(int(inp)):
        print(" "*x + "*")
        print(" "*(int(inp)-x) + "*")
        sleep(0.2/int(inp))
    for x in range(int(inp), 0, -1):
        print(" "*x + "*")
        print(" "*(int(inp)-x) + "*")
        sleep(0.2/int(inp))