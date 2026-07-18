test_values = [1, 2, 0, 4, 0, 5, 6]
result = []
count = 0
for value in test_values :
    if value !=0:
       result.append(value)
    else:
      count +=1
result = ([0] * count) + result
#result.extend([0] * count)
print(result)