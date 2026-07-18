num = int(input("Enter a number: "))
def get_fibonacci_series(num):
    fibo_ser =[]
    for i in range(num):
        if i == 0:
            fibo_ser.append(0)
        elif i == 1:
            fibo_ser.append(1)
        else:
            fibo_ser.append(fibo_ser[i-1] + fibo_ser[i-2])
    return fibo_ser
fibo_ser = get_fibonacci_series(num)
print("Fibonacci series up to ",fibo_ser)

