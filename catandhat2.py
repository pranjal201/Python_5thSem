cat = 0
hat = 0

str = input()

for i in range(0, len(str) - 2, 1):
    if(str[i:i+3] == "cat"):
        cat = cat + 1
    if(str[i: i+3] == "hat"):
        hat = hat + 1

if(cat == hat):
    print("True")
else:
    print("False")

    
