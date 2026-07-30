test_list =[1,2,4,3,2,7,5,1]

def remove_duplicate(test_list):
    res = []
    for i in test_list:
        if i not in res:
            res.append(i)
    print("The list after removing duplicates is", res)
    return res
remove_duplicate(test_list)
