def insertion(arr):
    for i in range(1,len(arr)):
        current_Ele =arr[i]
        pos = i
        while current_Ele < arr[pos-1] and pos > 0:
            arr[pos] = arr[pos-1]
            pos = pos -1

        else:
            arr[pos] =current_Ele

m = int(input())
arr =[int(i) for i in input().strip().split()]
insertion(arr)
print(i)




arr = [10,4,25,1,5]
print(insertion(arr))