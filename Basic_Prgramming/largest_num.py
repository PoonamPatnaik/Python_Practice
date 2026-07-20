# num_list = list(input("Enter a number"))
num_list =[3,2,1,7,10,4]
def find_larget_num(num_list):
    largest = 0
    for i in num_list:
        if int(i) > largest:
            largest = i
    print("The largest number is", largest)
def sort_list(num_list):
    n = len(num_list)

    # Traverse through all list elements
    for i in range(n):
        # Track if any swap occurs in this inner loop pass
        swapped = False

        # Last i elements are already in place, so skip them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                swapped = True

        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

    print("The sorted list is", num_list)
sort_list(num_list)
