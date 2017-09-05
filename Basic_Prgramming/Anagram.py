def verify_anagram(str1, str2):
        common_char, str_1, str_2 = check_commonString(str1, str2)
        if len(common_char)<=1:
            print(" Anagram can't be formed")
        else:
            print("Delete these charaters from string1"+" " +str(str_1))
            print("Delete these charaters from string1" + " "+ str(str_2))
            print("These characters makes Anagram"+ " "+str(common_char))
            count = len(str_1) + len(str_2)
            print (count)
            #print ("Total character to be deleted is : "+ count)


def  check_commonString(str1,str2):
     common_set ={}
     common_set = (set(str1)).intersection (set(str2))
     print common_set
     set_str1 = set(str1) - common_set
     set_str2 = set(str2) - common_set
     return common_set,set_str1,set_str2

verify_anagram("abcd","abcf")







