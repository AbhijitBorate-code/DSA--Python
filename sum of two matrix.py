


arr =   [[1,2,3 ],  # i is row  first multiplicatio of i * j
                    #  addition , sutraction is prit i +i
        [ 4 ,5,6],
        [7 ,8,9]]

nums = [[9,8,7],
        [6,5,4],
        [3,2,1]]

result =    [[0,0,0],
            [0,0,0],
            [0,0,0]]



for i in  range(len(arr)):
    # tme Complexity ( O(n2) )
    for j in  range(len(nums)):
        result[i][j] =arr[i][j] * nums[j][i]

for i in  result:
    print(i)