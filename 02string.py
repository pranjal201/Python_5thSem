# this program is about how string works in python

fruits = ['apple', 'banana', 'mango']

iter_obj = iter(fruits)
count = 0
while(count <  len(fruits)):
    print(next(iter_obj))
    count = count + 1
