# this program is about understanding polymorphism in pythonn
# it is achived by overloading and overriding.

# overriding is defining the method or variable again.
# overloading is achived by defining different parameters in the different methods with same name.

class Ninja:
    def __init__(self, name):
        self.name = name

    def Chakra(self):
        print("Every Ninja has some of 4 CHAKRA types")

class Uchiha(Ninja):
    def __init__(self, name, chakratype):
        self.chakratype = chakratype

        Ninja.__init__(self, name)

    def Chakra(self):
        print("{} has {} chakratype".format(self.name, self.chakratype))

class Senju(Ninja):
    def __init__(self, name, chakratype):
        self.chakratype = chakratype

        Ninja.__init__(self, name)

    def Chakra(self):
        print("{} has {} chakratype".format(self.name, self.chakratype))


if __name__ == "__main__":
    sen = Senju("Naruto", "Wind")
    sen.Chakra()
    
    uch = Uchiha("Sasuke", "Fire")
    uch.Chakra()
