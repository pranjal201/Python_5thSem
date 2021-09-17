class Student:

    school="St. Arnold's Hr. Sec. School"
    Class = "10th"
    
    def __init__(self, name):
        self.name = name

    def introduction(self):
        print(self.name)
        print(self.Class)
        print(self.school)


# creating objects
student1 = Student("Abhishek")
student2 = Student("Pranjal")

#calling methods
student1.introduction()
student2.introduction()
