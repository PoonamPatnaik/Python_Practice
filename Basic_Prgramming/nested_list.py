'''my_list =[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append([name, score])
print(my_list)'''


my_list =[["ram",15.5],["sita",18.5],["raghu",12.5]]
my_list.sort(key=lambda x: x[1])
print(my_list[0][0])