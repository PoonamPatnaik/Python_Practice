def factorial(n):
    mul =1
    for i in range(1,n+1):
        mul = mul *i
    print(mul)
num = int (raw_input())
factorial(num)