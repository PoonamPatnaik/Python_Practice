#given_list = (input("enter list number"))
given_list = [-1, 2, -3, 4, 0,-5, -6, -7, 2]
len_list =  len(given_list)
count = 0
i = 0
for i in range(len_list):
    #print('n',given_list[i])
    if (given_list[i] < 0) and (given_list[i-1] >= 0):
        given_list.insert(count, given_list[i])
        given_list.pop(i+1)
        count += 1
print(given_list)



