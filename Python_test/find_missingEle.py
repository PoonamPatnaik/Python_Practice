num = int(input())
total = sum(range(num+1))
print(total)
my_list = map(int,input().split())
l_total =0
for ele in my_list:
    l_total = ele + l_total
print(total - l_total)





