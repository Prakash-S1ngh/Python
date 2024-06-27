class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def insert(self , data):
        if(self.root is None):
            self.root = node(data)

        else:
           self.insert_recursive(self.root,data)

    def insert_recursive(self, Node, data):
        if data < Node.data:
            if Node.left is None:
                Node.left = node(data)
            else:
                self.insert_recursive(Node.left, data)
        elif data > Node.data:
            if Node.right is None:
                Node.right = node(data)
            else:
                self.insert_recursive(Node.right, data)



    def print1(self,root):
        if root is None:
            return 
        self.print1(root.left)
        print(root.data , end=" ->")
        self.print1(root.right)

    def printmax(self , root):
        if root is None:
            return -1
        return max(root.data , max(self.printmax(root.left) , self.printmax(root.right)))
    
    def printleftview(self , root):
        maxlevel = 0
        def printrecursive(root , level):
            nonlocal maxlevel
            if root is None:
                return
            if level > maxlevel:
                print(root.data , end=" ")
                maxlevel = level

            printrecursive(root.left , level+1)
            printrecursive(root.right , level+1)




        printrecursive(root , 1)

    def checkbalancetree(self , root):
        if root is None:
            return 0
        lft = self.checkbalancetree(root.left)
        rght = self.checkbalancetree(root.right)
        
        if abs(lft - rght)>1:
            return -1
        return max(lft , rght) + 1
    
    def maxwidth(self , root):
        maxi = 0
        list = []                               #declare an empty list
        list.append(self.root)

        while len(list)>=1:
            maxi = max(maxi , len(list))
            Node = list.pop(0)
            if Node.left is not None:
                list.append(Node.left)
            if Node.right is not None:
                list.append(Node.right)
           
                

        return maxi
    def ddlfrombt(self,root):
        prev = None    
    
        def bt_to_ddl(root ):
            nonlocal prev
            if root is None:
                return root
            head = bt_to_ddl(root.left)
            if prev is None:
                head = root
            else:
                root.left = prev
                prev.right = root
    
            prev = root 
            bt_to_ddl(root.right)
    
            return head
        curr = bt_to_ddl(root)
        while curr:
            print(curr.data , end=" <==> ")
            curr = curr.right
        
    

    # def deletion_in_tree(self,value):
    #     # Find the node to be deleted
    #     curr = self.root
    #     while curr.left or curr.right :
    #         if value < curr.left:
    #             curr = curr.left
    #         elif value == curr.value:
    #             break
    #         else:
    #             curr = curr.right

    #     if curr.left is None and curr.right is None:
    #         del curr
    #     else:
    #         curr1 = curr
    #         while curr1.left or curr1.right:
    #             if curr1.left is not None:
    #                 curr1 = curr1.left
    #             else:
    #                 curr1 = curr1.right
    #         temp = curr1
    #         curr1 = curr
    #         curr = curr1
            
            
        
            


list = [15,10,20,8,12,7,9,11,14,18,19,22,21,23]

Tree = tree()

for i in list:
    Tree.insert(i)

print("the original treee is :")

Tree.print1(Tree.root)
print()

print("the tree has max value is : ")
print(Tree.printmax(Tree.root))
print()
print("the leftmost view of a tree is :")
Tree.printleftview(Tree.root)
print()

if Tree.checkbalancetree(Tree.root) != -1:
    print("the tree is balanced ")
else:
    print("the tree is not balanced")

print('Maxwidth of the binary tree is :',Tree.maxwidth(Tree.root))

print("The double linkList from binary tree is :")
Tree.ddlfrombt(Tree.root)




        
            
