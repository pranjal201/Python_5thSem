# more deep dive into OOP

class Person:

    def __init__(self, name):
        self.name = name

    def isEmployee(self):
        return False

    def getName(self):
        return self.name

class Employee(Person):
    
    def isEmployee(self):
        return True

person = Person("Prateek")
emp = Employee("Raghav")

print("{}{}".format(person.getName(), person.isEmployee()))
print("{}{}".format(emp.getName(), emp.isEmployee()))

print(issubclass(Employee, Person))
print(issubclass(Person, Employee))

print(isinstance(emp, Employee))
print(isinstance(person, Person))
