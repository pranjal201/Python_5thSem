# this program is about encapsulation in oops

# Private = __name
# Protected = _name
# Public = name

class Base:
    def __init__(self):
        self.a = 5
        self.__c =10
        print("Parent{}".format(self.a))
        print("Parent{}".format(self.__c))

class child(Base):
    def __init__(self):
        self.b=11
        Base.__init__(self)
        print("Child{}".format(self.a))
        print("Child{}".format(self.b))

if __name__ == '__main__':
    obj1 = Base()
    obj = child()
    print(obj1._Base__c) # TICKY SYNTAX for accessing hidden variables in a class
    print(obj1)


