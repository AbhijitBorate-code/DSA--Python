"""def binary_search(arr, low, high, x):



    if high >= low:

        mid = (high + low) // 2


        if arr[mid] == x:
            return mid


        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)


        else:
            return binary_search(arr, mid + 1, high, x)

    else:

        return -1
"""



def binarray_search(arr , low , higth , x):

    while low <= higth:

        mid = (low + higth) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:

             higth = mid - 1
        else:
            low = mid +  1

    return -1

arr = [3,6,8,9,10,21,31,32]
low= 0
higth = len(arr)-1
x = 31
print(binarray_search(arr ,low , higth ,x))
"""


























arr = [1, 2, 3, 4, 5, 13] | low = 0 | higth = 5 | x = 4

        |           |
        |           |
mid = 2 | mid = 4   | mid = 3
        |           |
        |           |
        |           | return 3
        |           |
        |           |
low = 3 |           |
        |           |
        | higth = 3 |


arr = [1, 2, 3, 4, 5, 13]
low = 0
higth = 5
x = 4
print('3')
"""