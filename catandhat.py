# to find the particular work cat and hat repetition in string

str = input()
print(str)

cat = "cat"
count = 0
catcount = 0
i = 0
c = 0
while (i < len(str)):
    while (c < len(cat)):
        if(str[i] == cat[c]):
            count = count + 1
            c = c + 1
        if(count == len(cat)):
            catcount = catcount + 1
            c = 0
            count = 0
        i = i+1
        if(i == len(str)):
            break

print(catcount)
i = 0
h = 0
hat = "hat"
hatcount = 0
while (i < len(str)):
    while (h < len(hat)):
        if(str[i] == hat[h]):
            count = count + 1
            h = h + 1
        if(count == len(hat)):
            hatcount = hatcount + 1
            h = 0
            count = 0
        i = i+1
        if(i == len(str)):
            break
print(hatcount)
