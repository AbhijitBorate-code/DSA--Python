def Quick_sort(arr, start , end):
    pivot = arr[start]
    left = start +1
    right =  len(arr)-1

    while True:

        while left <= right and arr[left] <=pivot:
            left = left+1
        while left <= right and arr[right] >=pivot:
            right =right + 1
        if right < right:
            break

        else:
            arr[left],arr[right] = arr[left] , arr[right]
        arr[start], arr[right] = arr[right], arr[start]
    return right


def quicksor(arr, start , end):
    if start < end:
        p= Quick_sort(arr, start , end)
        quicksor(arr,start,p-1)
        quicksor(arr,p+1,end)


arr =[56,12 ,34, 56, 90]
quicksor(arr ,0,len(arr)-1)
print(arr)




