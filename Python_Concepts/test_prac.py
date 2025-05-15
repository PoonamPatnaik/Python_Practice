

n = int(input("enter a number"))
if (1 <= n <= 100):
    if ((n % 2 != 0) or ((5 < n < 21) and (n % 2 == 0))):
        print("Weird")
    elif ((1 < n < 6) and (n % 2 == 0)) or ((n % 2 == 0) and n > 20):
        print("Not Weird")
else:
    print("Invalid argument")
