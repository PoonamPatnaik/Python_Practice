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


# 3 ways to reverse a string: while, for loop, slicing.. Calling functions
#while_reverse_str(name)
#for_reverse_str(name)
silcing_reverse_str(name)