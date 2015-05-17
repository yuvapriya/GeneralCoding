def partition(arr, left, right, pivot):
    pivotValue = arr[pivot]
    print 'Chosen pivotIndex is',pivot,' and pivotValue',pivotValue
    print 'left:',left,'right:',right
    print 'Array to start with is', arr
    # Move pivot to end
    temp = arr[pivot]
    arr[pivot] = arr[right]
    arr[right] = temp
    storeIndex = left
    print 'Array after moving pivot to end is', arr
    # Run loop from left to element before pivot
    for i in range(left,right):
        if(arr[i]<pivotValue):
            print 'storeIndex',storeIndex,'i:',i
            temp = arr[storeIndex]
            arr[storeIndex] = arr[i]
            arr[i] = temp
            storeIndex+=1
    # Swap the pivot element back
    temp = arr[storeIndex]
    arr[storeIndex] = arr[right]
    arr[right] = temp
    print 'Array is now', arr
    return storeIndex

# kth Smallest
def kthSelect(arr, left, right, k):
    if left == right:
        return arr[left]
    pivotIndex = (left + right) /2    
    pivotIndex = partition(arr, left, right, pivotIndex)
    print 'newPivotIndex',pivotIndex
    if(pivotIndex == k):
        return arr[pivotIndex]
    elif k < pivotIndex:
        return kthSelect(arr, left, pivotIndex - 1, k)
    else:
        return kthSelect(arr, pivotIndex + 1, right, k)

  
arr = [5,4,3,2,8,6,7]
arr = [10,3,9,1,4,5,7,8]
print kthSelect(arr,0,len(arr)-1,3)