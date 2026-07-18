input_user_num = int(input("Enter the number of prime numbers you want to print: "))
def check_num_prime(num):
    if num >1:
        for i in range(2,int((num/2)+1)):
            if num % i == 0:
                return False
        return True
    elif num ==1:
        return True
    else:
        return False
for i in range(input_user_num):
    if check_num_prime(i)==True:
        print(i)
