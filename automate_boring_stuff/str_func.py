name = input("Enter name")

def rev_str(actual_string):
    rev_name = ""
    len_strg = len(actual_string)
    for i in range(len_strg):
        print(i,len_strg-i)
        rev_name = rev_name + name[len_strg - i - 1]
        print(rev_name)
    return rev_name
reversed_name = rev_str(name)
print("reverse name is: " + reversed_name)
new_name = input("Enter name")
new_len_strg = len(new_name)
def rev_string_m(str_len):
    rev_name = ""
    while str_len > 0:
        rev_name = rev_name + new_name[str_len-1]
        str_len = str_len-1
    return rev_name