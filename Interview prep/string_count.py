str_test= "my name is poonam and my hobby is reading"
updated_str = str_test.split(" ")
print (updated_str)
test_dict = {}
count = 0
len_str = len(updated_str)
for i in range(len_str):
    if updated_str[i] in test_dict.keys():
           test_dict[updated_str[i]] +=1
    else:
        print(updated_str[i])
        test_dict[updated_str[i]] = 1
print (test_dict)