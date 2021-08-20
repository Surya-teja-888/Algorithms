# Quick sort Algorithm
# Last element as pivot

# To get the correct position of pivot element
def pivot_place(list1,first,last):
    pivot = list1[first] # first element as pivot
    left = first+1 #  indexing left
    right = last # indexing right
    while True:
        while left <= right and list1[left] <= pivot:
            left = left + 1
        while left <= right and list1[right] >= pivot:  
            right = right - 1
        if left > right:
            break
        else:
            list1[left],list1[right] = list1[right],list1[left]
    list1[first],list1[right] = list1[right],list1[first] 
    return right 

def quicksort(list1,first,last):
    if first<last:
        p = pivot_place(list1,first,last) 
        quicksort(list1,first,p-1) # dividing into sublist
        quicksort(list1,p+1,last) # dividing into sublist

list1 = [56,26,93,17,32,44]
n = len(list1)
quicksort(list1,0,n-1)
print(list1)









        







        





