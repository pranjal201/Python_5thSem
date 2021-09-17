valid = True
if (valid):
    print("Pranjal")

print(valid == True)
print(valid == False)

print(bool(0) != True)
print(bool(1) == False)

num = bin(8)
print(num)
print(num[2:].rjust(4, "|"))

x = 13
y = 5
print(bin(x)[2:].rjust(4, "0"))
print(bin(y)[2:].rjust(4, "0"))


print(bin(x & y)[2:].rjust(4, "0"))
print(bin(x | y)[2:].rjust(4, "0"))


# shift operators

num = 14
print(bin(num))
print(bin(num)[2:].rjust(4, "0"))
print(bin(num << 4)[2:].rjust(4, "0"))

print(bin(9 << 3))
