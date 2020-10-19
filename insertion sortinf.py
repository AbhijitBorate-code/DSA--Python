
def insertion_sort(arr):
    for i in range(len(arr)-1):
        current = arr[i]
        pos = i
        while current < arr[pos-1] and pos > 0:
            arr[pos] = arr[pos-1]
            pos = pos-1
        else:
            arr[pos] =current






arr = [5,3,2,6,7,1]
insertion_sort(arr)
print(arr)