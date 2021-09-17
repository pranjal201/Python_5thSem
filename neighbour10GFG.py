N = int(input())
quotient = N/10
mul1 = quotient * 10
mul2 = (quotient + 1) * 10
if((N >= mul1) and (N<=mul1+2)):
    print("True") 
elif((N <= mul2) and (N>=mul2-2)):
    print("True")
else:
    print("False") 
