def binary_search(arr, target,left,right):

    if left> right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,right)
    else:
        return binary_search(arr,target,left,mid-1)


arr = [2, 5, 7, 9, 12, 15, 20]
print(binary_search(arr, 12, 0, len(arr)-1))
