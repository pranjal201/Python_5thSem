def squaregenerator():
    i = 1

    while True:
        yield i*i

        i = i+1


for i in squaregenerator():
    if(i > 100):
        break
    print(i)
