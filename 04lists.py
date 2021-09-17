matrix = [[1,2,3], [4,5,6], [7,8,9]]
newMatrix = []

for i  in matrix:
    for j in i:
        newMatrix.append(j)

print(newMatrix)

# the above code can be written as

flat_matrix = [val for subval in matrix for val in subval]
print(flat_matrix)

planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter','Saturn'], ['Uranus', 'Neptune', 'Pluto']]

newPlanets = [val for subval in planets for val in subval if(len(val) < 6)]
print(newPlanets)

