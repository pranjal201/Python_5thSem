""" 
This is list comprehension
"""

matrix = []
for i in range (6):
    matrix.append([])
    matrix[i] =[a for a in range(5)]

for i in matrix:
    print(i)

# the above code can be wriiten as
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)
