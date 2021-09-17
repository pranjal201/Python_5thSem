# enumerating in python

characters = ["Gojo", "Itadori", "Megumi", "Nobara"]

print(len(characters))

for i in characters:
    print(i)

# indexing method
for i in range(len(characters)):
    print(characters[i], end=">")

print()


# enumerating method

one_piece = ["Luffy", "Zoro", "Sanji", "Nami", "Chopper", "Brook", "Nami", "Robin", "Jinbie", "Franky"]

for i, x in enumerate(one_piece):
    print(i, x)

for i in enumerate(one_piece):
    print(i[0], i[1])
