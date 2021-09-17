count = 0

str = input()

for i in range(0, len(str)-3, 1):
    if((str[i:i+2] == "do") and (str[i+3] == "e")): 
        count += 1
 #   if(str[i+3] == "e"):
  #      count += 1

print(count)

string1 = "PRanjal"
print(string1)
string1 =string1[1:4]
print(string1)
