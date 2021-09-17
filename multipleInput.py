print("Enter the number:")
num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)


x, y = [int(x) for x in input().split()]
print(x + y)

a, b = map(int, input().split())
print(a + b)
