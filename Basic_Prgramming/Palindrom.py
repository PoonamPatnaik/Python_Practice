def verify_palindrom(str_copy):
    if str_copy == str_copy[::-1]:
        print ("YES")
    else:
        print ("NO")
str_copy = (input("enter a string"))
verify_palindrom(str_copy)