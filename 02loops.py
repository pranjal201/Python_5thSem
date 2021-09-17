to_do = ["Bath", "Meet", "Dance"]
print("*" * 3 + "List" + "*" * 3)
for i in to_do:
    print("*" + i)

to_tuple = ("geeks", "cube", "cyber")
print("this is tuple")
for i in to_tuple:
    print(i)

to_dict = {"name": "Pranjal", "class": "IT-B", "colleg": "SVVV"}
for i in to_dict:
    print("%s- %s" % (i, to_dict[i]))
