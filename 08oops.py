# using of super keyword in python

class Parent:
    def __init__(self, name):
        print("Parent:{}".format(name))

  
class Child(Parent):
    def __init__(self):
        print("This is Child")
        super().__init__("MAX")
      
       
obj1 = Child()
print(Child.__mro__)

# __mro__ gives the sequence of method search 
# MRO - Method Resolution Order
