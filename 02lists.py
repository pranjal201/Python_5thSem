#this program is list comprehension

# it is like adding condition inside list
odd_aquare = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_aquare)

poweroftwo = [2 ** i for i in range(1, 11) ]
print(poweroftwo)

sentence = "My number is 9630924953"
numExtractor =  [x for x in sentence if x.isdigit()]

print(numExtractor)
