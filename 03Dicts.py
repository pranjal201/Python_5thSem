arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

from collections import Counter

common = []
arr1 = Counter(arr1)
arr2 = Counter(arr2)
arr3 = Counter(arr3)

resultDict = dict(arr1.items() & arr2.items() & arr3.items())
for key, val in resultDict.items():
    common.append(key)

print(common)
