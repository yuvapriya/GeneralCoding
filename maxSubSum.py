def maxSubSum(arr):
    max_ending_here = max_so_far = 0
    for i in range(len(arr)):
        max_ending_here = max(0,max_ending_here + arr[i])
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far
    
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print maxSubSum(arr)