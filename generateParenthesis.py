def addParenth(list, leftRem, rightRem, str, index):
    if(leftRem<0 or rightRem<leftRem):
        return
    if(leftRem==0 and rightRem ==0):
        list.append(''.join(str))
    else:
        if(leftRem > 0):
            str[index]='('
            addParenth(list, leftRem-1, rightRem, str, index+1)
        if(rightRem > 0):
            str[index]=')'
            addParenth(list, leftRem, rightRem-1, str, index+1)
            
def generateParenth(count):
    str = []
    for i in range(count*2):
        str.append('')
    list = []
    addParenth(list, count, count, str, 0)
    print list
generateParenth(3)