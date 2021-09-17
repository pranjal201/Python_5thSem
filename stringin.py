string1 = "This is a string"
string2 = 'This is a string too!'
print(string1)
print(string2)

print(type(string1))
print(type(string2))


string3 = """This is
a multi
line
string"""
print(string3)

string4 = "I\'m a string"
print(string4)

string5 = "\x41\x42"
print(string5)

string6 = 'a' * 30
print(string6)

print(len(string6))
print(len(string5))

intro = "My name is Pranjal Parmar"
print("Pranjal" in intro)
print(intro.startswith("P"))
print(intro.startswith("M"))

print(intro.index("Pranjal"))

print(intro.upper())
print(intro.lower())

print(intro.find("Parmar"))


print(string4.split())
print(intro.split())

string_space = "       Spacey       "
print(string_space)
print(string_space.strip())

print(intro.replace(" ", "|"))
print(intro.replace("Pranjal", "Praveen"))

# justified function

print(intro.rjust(60, "|"))

print("|" * 10 + "cube" + "|" * 10)
print(intro.ljust(60, "|"))

length = "Saturo Gojo"
print(f"Main hero is : {length}")
