num_list= [3,4,8,1,6,4,7]
sum_val = 8
# expected output [(1,5),(3,6)]
def sum_return_index(num_list):
    result = []
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == sum_val:
                result.append((i, j))
    return result
print(sum_return_index(num_list))