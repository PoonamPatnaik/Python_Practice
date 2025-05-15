l = [1,3,4,5]
l2 = [2,6]
update_l = sorted(l)
update_l2 = sorted(l2)
update_list = (update_l+update_l2)
print(update_list)
for i in range(len(update_list)):
   if (update_list [i]>update_list[i+1]):
    update_list[i+1] = update_list [i]
   print(update_list)
