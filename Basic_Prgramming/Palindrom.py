def verify_palindrom(str_copy):
    if str_copy == str_copy[::-1]:
        print ("YES")
    else:
        print ("NO")
def check_palidrom(str_copy):
    reversed_str =""
    leng_str = len(str_copy)
    for i in range(leng_str):
        reversed_str = reversed_str + str_copy[leng_str - i - 1]
    if str_copy == reversed_str:
        print ("YES")
    else:
        print ("NO")
        print(reversed_str)



str_copy = (input("enter a string  "))
check_palidrom(str_copy)