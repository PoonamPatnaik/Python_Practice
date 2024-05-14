num = int(input("Enter a number"))
for i in range (2,int(num/2)):
    if num % i == 0:
        print("Number is not Prime")
        break
else:
        print("Number is Prime")