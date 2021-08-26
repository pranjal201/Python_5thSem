# 1
# 2 2
# 3 3 3
print("Enter the numbers of rows you want to print:")

rows = int(input()) 

i, j = 0, 0
for i in range(1, rows+1):
    for j in range(0, i):
        print(i, end=" ")

    print()
