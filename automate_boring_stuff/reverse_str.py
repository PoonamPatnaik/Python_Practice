
def while_reverse_str(name):
    str_len = len(name)
    rev_name = ''
    while str_len > 0:
        rev_name = rev_name + name[str_len-1]
        str_len = str_len-1
    print("Reverse string is ",rev_name)
def for_reverse_str(name):
    rev_name = ''
    for cha in name:
        rev_name = cha + rev_name
    print("Reverse string is ",rev_name)

def silcing_reverse_str(name):
    rev_name = name[::-1]
    print("Reverse string is ",rev_name)

name = input("Enter the Name")
print("Actual name is :" + name)
# 3 ways to reverse a string: while, for loop, slicing
#while_reverse_str(name)
#for_reverse_str(name)
silcing_reverse_str(name)






'''
name = input("Enter the Name")
print("Actual name is :" + name)
r_name = ""
for char in name:
    print(char)
    r_name = char+r_name
print("Reversed string is "+r_name)
def rev_str(len_strg):
    rev_name = ""
    for i in range(len_strg):
        print(i,len_strg-i)
        rev_name = rev_name + name[len_strg - i - 1]
        print(rev_name)
    return rev_name
reversed_name = rev_str(len_strg)
print("reverse name is: " + reversed_name)

new_name= input("Enter name is :")
print("New name is" + new_name)
new_len_strg = len(new_name)
def rev_string_m(str_len):
    rev_name = ""
    while str_len > 0:
        rev_name = rev_name + new_name[str_len-1]
        str_len = str_len-1
    return rev_name
reversed_nname = rev_string_m(new_len_strg)
print("reverse name is: " + reversed_nname)
'''

