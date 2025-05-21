n = int(input("Enter a number"))
if (1<=n<=150):
    i =1
    for i in range (n):
        i += 1
        print(i,end = "")
else:
    print("Invalid input")