list1 = [1,8,6,2,0]
print(list1)
for i in range(len(list1)):
    min_val = min(list1[i:])
    print(min_val)
    min_index = list1.index(min_val)
    list1[i] ,list1[min_index] = list1[min_index],list1[i]
print(list1)
