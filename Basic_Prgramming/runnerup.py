n = int(input())
arr = map(int, input().split(","))
sort_arr= sorted(set(arr))
print(sort_arr[-2])