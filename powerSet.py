def powerSet(arr):
    l = 2 ** len(arr)
    for i in range(l):
        print generateSet(i, arr)

def generateSet(i, arr):
    genSet = []
    for x in range(len(arr)):
        if ( i >> x) % 2 == 1:
            genSet.append(arr[x])
    return genSet
    
powerSet(['a','b','c'])