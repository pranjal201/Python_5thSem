# TabNine::sem


print("what is the fucking Problem")

para1 = """ Hacker was first used in the 1960s to describe a programmer or an individual who, in an era of highly constrained computer capabilities, could increase the efficiency of computer code in a way that removed, or hacked, excess machine code instructions from a program. It has evolved over the years to refer to someone with an advanced understanding of computers, networking, programming or hardware.
"""
index = para1.find("hack", 4)
print(para1[index])
print(para1[index+1])
print(para1[index+2])
print(para1[index+3]) 


string = "Pranjal"
sentence = "Pranjalis a good boy, There is a nice scenery out there"

print(sentence.find("Pranjal",0))

print(sentence.startswith("Pranjal"))

NAME = "Pranjal"
print(NAME.lower())
print(NAME.upper())
print(NAME.swapcase())
print(sentence.title())
