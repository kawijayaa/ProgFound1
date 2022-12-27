def myF(number1 = 0, number2 = 50):
    print("In myFunction:")
    print("Before exchange:", number1, number2)
    number1, number2 = number2, number1
    print("After exchange:", number1, number2)

def main():
    number1 = 12
    number2 = 25
    myF(number1, number2)
    print("In main:", number1, number2)
    myF(number1)
    print("In main:", number1, number2)
    myF()
    print("In main:", number1, number2)
    myF(number2=number1, number1=number2)
    x = (2,3)
    myF(*x)
    myF(x)

main()    

class Counter(object):
    def __init__(self):
        self.count = 0
    
    def click(self):
        self.count += 1
    
    def getValue(self):
        print(self.count)

    def reset(self):
        self.count = 0
    

tally = Counter()
tally.click()
tally.getValue()
tally.getValue()

class Student(object):
    pass

class UIStudent(Student):
    pass

a = UIStudent()
print(isinstance(a, Student))

a = [1,2,3]
b = [1,2,3]

print(a is b)