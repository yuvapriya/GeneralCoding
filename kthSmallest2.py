from random import randrange
import sys
sys.setrecursionlimit(1000)
def partition(arr, pivot, start, end):
    inc_idx = start
    val = arr[pivot]
    #swap pivot and last element
    arr[end],arr[pivot] = arr[pivot], arr[end]
    for i in range(start,end):
       if(arr[i]<=val):
           arr[inc_idx],arr[i] = arr[i], arr[inc_idx]
           inc_idx += 1
    arr[end],arr[inc_idx] = arr[inc_idx],arr[end]
    return inc_idx
    
def kthSmallest(arr, k, start, end):
    pivot_ridx = k
    pivot = arr[pivot_ridx]
    pivot_idx = partition(arr, pivot_ridx, start, end)
    print 'Chosen:',pivot,'at',pivot_ridx,'actually at:',pivot_idx
    if(pivot_idx + 1 ==k):
        return pivot
    elif(pivot_idx + 1 > k):
        return kthSmallest(arr, k, start, pivot_idx)
    else:
        return kthSmallest(arr, k, pivot_idx, end)
            
arr = [2,1,4,5,3]
k = 3
start = 0
end = len(arr) - 1
print kthSmallest(arr, k ,start, end)  

from random import randrange

def findKMin(arr,k,start=0,end=None):
    '''
    Find kth minimum element in a array (in-place randomized algorithm, similar to quicksort)
    assumption: Input will only contain unique elements'''
    if k > len(arr):
        raise Exception("k should be less than length of the input array")
    if not end: end = len(arr) -1 #Get last index value
    pivot_ridx = k     #Get a random array element as pivot value
    pivot = arr[pivot_ridx]
    pivot_idx = partition(arr,start,end,pivot_ridx) #partition to partition array around the pivot value in place
    print 'Chosen:',pivot,'at',pivot_ridx,'actually at:',pivot_idx
    if pivot_idx+1 == k:
        return pivot #Well, there is your answer
    elif pivot_idx+1 > k:
        return findKMin(arr,k,start,pivot_idx) #lies somewhere in the first partition
    else:
        return findKMin(arr,k,pivot_idx,end) #lies somewhere in the second Partiton

def partition(arr,start,end,pivot_idx):
    '''
    Partitions array in-place around the given pivot value
    '''
    pivot = arr[pivot_idx]
    arr[end],arr[pivot_idx] = arr[pivot_idx],arr[end]
    inc_idx = start
    for i in xrange(start,end):
        if arr[i] <= pivot:
            arr[inc_idx],arr[i] = arr[i],arr[inc_idx]
            inc_idx+=1
    arr[end],arr[inc_idx] = arr[inc_idx],arr[end]
    return inc_idx
arr = [2,1,4,5,3]
k = 3
#print findKMin(arr,k)