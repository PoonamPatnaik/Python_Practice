num = int(input())
my_list = input().split()
my_list = [int(i) for i in my_list]


x = len(my_list)

for i in range(x-1):
    total = my_list[i]

    for j in range (i+1,x):
        total = total + my_list[j]
        if total >= num:
            if total == num:
                print(my_list[i],my_list[j])
                break