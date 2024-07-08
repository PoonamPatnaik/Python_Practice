import math
num = int (input("enter a number"))
def factorial_math(num):
    fac_val = math.factorial(num)
    print(fac_val)

def factorial(n):
    mul =1
    for i in range(1,n+1):
        mul = mul *i
    print(mul)

factorial(num)
factorial_math(num)