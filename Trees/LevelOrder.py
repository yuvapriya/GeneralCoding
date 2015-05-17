class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def setRight(self, n):
        self.right = n
        
    def setLeft(self, n):
        self.left = n
        
class Tree:        
    def printLevelOrderTree(self,root):
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
            
    def isBST(self,node):
        if node == None:
            return 1
        if node.left != None and node.left.data > node.data:
            return 0
        if node.right != None and node.right.data < node.data:
            return 0
        if self.isBST(node.left) == 0 or self.isBST(node.right) == 0:
            return 0
        return 1
            
a = Node(10)
b = Node(7)
c = Node(12)
d = Node(6)
e = Node(8)
f = Node(11)
g = Node(13)
a.setLeft(b)
a.setRight(c)
b.setLeft(d)
b.setRight(e)
c.setLeft(f)
c.setRight(g)
t= Tree()
t.printLevelOrderTree(a)
print t.isBST(a)
