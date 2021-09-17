# this will be the practice of the oops conceps in python

class Dog:
    breed = "Labrador"

    def __init__(self, name):
        self.name = name


Kalu = Dog("Kalu")
Shelu = Dog("Shelu")

print("Kalu  is a {}".format(Kalu.__class__.breed))
print("Shelu  is a {}".format(Shelu.__class__.breed))

print("My name is {}".format(Kalu.name))

print("My name is {}".format(Shelu.name))
