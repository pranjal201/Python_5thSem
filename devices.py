# TabNine::sem
# creating laptops
import string
from random import choice
from tabulate import tabulate
def create_laptops(number=1):
    laptops = list()
    
    
    for i in range(0,number):
    
        laptop = dict()
    
        laptop["name"] = (choice(string.ascii_letters)+choice(string.ascii_lowercase)+choice(string.ascii_uppercase)+str(i))
    
        laptop["OS"] = choice(["Windows", "Linux", "MacOSX"])
    
        if(laptop["OS"] == "Windows"):
            laptop["Vendor"] = choice(["Dell", "HP", "Lenovo"])
            laptop["version"] = choice(["11", "10", "8", "7 ultimate"])
    
        if(laptop["OS"] == "Linux"):
            laptop["Vendor"] = choice(["System76", "Dell"])
            laptop["version"] = choice(["Ubuntu", " Debian", "Kal"])
    
        if(laptop["OS"] == "MacOSX"):
            laptop["Vendor"] = "Apple"
            laptop["version"] = choice(["catilana", "Serria", "Macintosh"])
        laptops.append(laptop)

    return laptops
    
print(__name__)
    
#--------------------MAIN PROGRAM -------------------------------------------
if __name__ == "__main__":
    number = int(input("Enter the number of laptop you want to generate"))
    created_laptops = create_laptops(number)
    print(tabulate(created_laptops, headers="keys"))
    
