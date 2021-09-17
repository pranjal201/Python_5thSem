'''Input:
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Q = [3, 6, 8, 12]
Output:
True
True
True
False
Explanation:
Since 3, 6, 8 are preset in the given
list and 12 is not present.]]'''

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Q = [3, 6, 8, 12]
print(type(Q))
for i in range(len(num_list)):
    num_list[i]
    if(num_list[i] in Q):
        print("True")
print("False")
