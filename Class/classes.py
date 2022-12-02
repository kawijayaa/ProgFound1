class Person:
    def __getInfo(self):
        return "Person"

    def printPerson(self):
        print(self.__getInfo())
    
class Student(Person):
    def __getInfo(self):
        return "Student"

Person().printPerson()
Student().printPerson()