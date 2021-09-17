# TabNine::sem
str1 = "Pranjal Parmar surname is Parmar"

# 
# str2 = "Praveen"
# 
# print(str1.replace("Parmar", str2, 1))
# 
# list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# print(list1[:1])
# list1[:1] = str1
# print(list1)

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(list1[:7])

for i in list1:
    print(i+"-"+str(list1.index(i)))
list1[:0] = str1


for i in list1:
    print(i+"-"+str(list1.index(i)))


