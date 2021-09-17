# applying mutiple inheritance in python

class Woman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print("This is from class Woman")
        return self.name
    def get_age(self):
        print("This is from class Woman")
        return self.age
class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print("This is from class Man")
        return self.name

    def get_age(self):
        print("This is from class Man")
        return self.age


class Employee(Woman, Man):
    def __init__(self, name, age, job):

        self.job = job

        Man.__init__(self, name, age)
        Woman.__init__(self, name, age)

        def showdata(self):
            print("{} {} {}".format(self.name, self.age, self.job))


emp1 = Employee("Pranjal", 20,"employeed")
print(emp1.get_name())
print(emp1.get_age())

print(Employee.__mro__)
