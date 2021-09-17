# static var or class variables
# instance variable

class SVIIT:
    def __init__(self, name):
        self.name = name


class ComputerScience(SVIIT):
    CS = 0
    @staticmethod
    def incrementor():
        ComputerScience.CS += 1
    def __init__(self, name, branch):
        self.branch = branch
        SVIIT.__init__(self,name)
        ComputerScience.incrementor()

class InformationTechnology(SVIIT):
    IT = 0 
    @staticmethod
    def incrementor():
        InformationTechnology.IT += 1
    def __init__(self, name, branch):
        self.branch = branch
        SVIIT.__init__(self,name)
        InformationTechnology.incrementor()

student1 = InformationTechnology("Prateek", "IT")
print(student1.IT)

student2 = InformationTechnology("Pranjal", "IT")
print(student2.IT)
student3 = InformationTechnology("Raghav", "IT")
print(student3.IT)

print(student1.IT)
student4 = ComputerScience("Piyush","CS")
print(student4.CS)

