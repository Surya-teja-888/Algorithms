# Initializing List
list1 = [3,8,21,90,1,100]

# Algorithm
for i in range(len(list1)):
    min_value = min(list1[i:])
    min_index = list1.index(min_value)
    list1[i],list1[min_index] = list1[min_index],list1[i]

print(list1)     

