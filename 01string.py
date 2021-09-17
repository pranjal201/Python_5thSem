
name = "Pranjal"

for letters in name:
    if(letters != 'l'):
        print(letters)


for letters in name:
    if(letters != 'a'):
        print(letters)

name = "Pranjal Parmar is a good boy"
for letters in name:
    if(letters == " "):
        print("*", end="")
    else:
        print(letters, end="")

print()


for letters in name:
    pass
print(f'Last  letter is {letters}')
