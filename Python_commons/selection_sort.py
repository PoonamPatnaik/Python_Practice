def selection_sort(l1):
    n= len(l1)
    for i in range(n-1):
        min_val= i
        for j in range(i+1,n):
            if l1[j]<l1[min_val]:
               min_val = j
        l1[i],l1[min_val] = l1[min_val],l1[i]
    print(l1)


list1 = [6,4,9,7,8]
selection_sort(list1)
