# 3 3 3
# 2 2
# 1

print("Enter the number of rows:",end="")
row = int(input())

while(row > 0):
    col = 0
    while(col < row):
        print(row, end=" ")
        col = col + 1
    print()
    row = row - 1
