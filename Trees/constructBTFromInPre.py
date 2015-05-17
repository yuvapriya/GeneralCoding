class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def setRight(self, n):
        self.right = n
        
    def setLeft(self, n):
        self.left = n
      
def printLevelOrderTree(root):
    q=[]
    q.append(root)
    while len(q)>0:
        thisLevel = q
        q=[]
        for n in thisLevel:
            print n.data,
            if n.left!= None:
                q.append(n.left)
            if n.right!=None:
                q.append(n.right)
        print     

def findIndex(arr, data):
    for i in range(len(arr)):
        if data == arr[i]:
            return i
    return -1
    
def constructBT(inOrder, preOrder):
    if(len(inOrder) == 0 or len(preOrder)==0):
        return
    rootData = preOrder[0]
    root = Node(rootData)
    inOrderIndex = findIndex(inOrder, rootData)
    leftInOrder = inOrder[0:inOrderIndex]
    rightInOrder = inOrder[inOrderIndex + 1:]
    leftPreOrder = preOrder[1:len(leftInOrder)+1]
    rightPreOrder = preOrder[len(leftInOrder)+1:]
    root.setLeft(constructBT(leftInOrder, leftPreOrder))
    root.setRight(constructBT(rightInOrder, rightPreOrder))
    return root

inOrder = 'DBEAFCG'
preOrder = 'ABDECFG'

root = constructBT(inOrder, preOrder)
printLevelOrderTree(root)
        
    
    