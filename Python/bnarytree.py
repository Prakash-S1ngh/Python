class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class tree:
    def __init__(self):
        self.root = None

    

    def recursiveinsertion(self ,root , data):
        if root is None:
            return node(data)
        

        if root.data > data:
            root.left = self.recursiveinsertion(root.left,data)

        elif root.data<data:
          root.right  =   self.recursiveinsertion(root.right,data)

        return root
    
    def insert(self , data):
        if self.root is None:
            self.root =  node(data)
        
        else:
             self.recursiveinsertion(self.root , data)
        
    def printtree(self,root):
        if root is None:
            return 
        self.printtree(root.left)
        print(root.data , end="-> ")
        self.printtree(root.right)


    def deletion(self , root,val):
        if root is None:
            return root
        
        if val<root.data:
            root.left = self.deletion(root.left , val)
        elif root.data<val:
            root.right = self.deletion(root.right , val)


        else:
            if root.left is None and root.right is None:   # deletion of node with no child
                return None
            
            elif root.left is None:         #deletion of node with one child
                temp = root.right
                root=None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            else:
                root.data = self.preordersuccessor(root.left)       # deletion of node with two child
                root.left = self.deletion(root.left , root.data)     # deletion of predecessor

        return root
                 
 

    def preordersuccessor(self , root):
        curr = root
        
        while  curr.right is not None:
            curr = curr.right

        return curr.data
            
        
            
        
        
bst = tree()

list = [8,3,10,1,6,4,7,14,9,13,15]

for i in list:
    bst.insert(i)

print(bst.printtree(bst.root))
bst.deletion(bst.root , 14)

print(bst.printtree(bst.root))
bst.deletion(bst.root , 8)
            
print(bst.printtree(bst.root))