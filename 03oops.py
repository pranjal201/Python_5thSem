# this program is about inheritance
from random import choice

class Mammal:
    def __init__(self, name):
        self.name = name

    def actionPerformed(self):
        self.action = choice(["Sleeping", "Eating", "Playing"])
        print("{} is {}".format(self.name, self.action))    

class Dog(Mammal):

    def __init__(self, name, breed):
        self.breed = breed

        Mammal.__init__(self, name)
    def about(self):
        print("{} is a {}".format(self.name, self.breed))


class Cat(Mammal):
    def __init__(self, name, breed):
        self.breed = breed

        Mammal.__init__(self, name)

    def about(self):
        print("{} is a {}".format(self.name, self.breed))

kalu = Dog("kalu", "Desi")
kuty = Cat("kuty", "Videsi")

kalu.about()
kalu.actionPerformed()

kuty.about()
kuty.actionPerformed()
