
def bubble_sort(l1):
    n = len(l1)
    for i in range(n-1):
        for j in range(n-1-i):
            if l1[j] > l1[j+1]:
                l1[j],l1[j+1] = l1[j+1],l1[j]
    print(l1)

list1 = [2,4,3,7,8]
bubble_sort(list1)