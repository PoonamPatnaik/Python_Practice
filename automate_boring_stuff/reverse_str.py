name = input("Enter the Name")
print("Actual name is :" + name)
len_strg = len(name)
rev_name =""
while len_strg >0:
    rev_name = rev_name + name[len_strg-1]
    len_strg = len_strg-1
print("Reversed name is:" +rev_name)