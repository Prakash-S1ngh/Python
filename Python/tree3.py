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


# print the tree level by level 
    def printlevel(self , root):
        if root is None:
            return 
        
        list = []
        list.append(self.root)
        while len(list)>0:
            Node = list.pop(0)
            print(Node.data , end=" ")
            if Node.left is not None:
                list.append(Node.left)
            if Node.right is not None:
                list.append(Node.right)

    def printnextlevel(self , root):
        if root is None:
            return 
        list = []
        list.append(self.root)

        while len(list) > 0:
            count = len(list)
            for i in range(count):
                Node = list.pop(0)
                print(Node.data,end=" ")
                if Node.left is not None:
                    list.append(Node.left)
                if Node.right is not None:
                    list.append(Node.right)
            print()

             
        




list = [12,10,13,9,11,12,14]

Tree = tree()

for i in list:
    Tree.insert(i)

Tree.print1(Tree.root)
# print("the tree is printed level by level : ")
# Tree.printlevel(Tree.root)
print("the tree is printed level by level with new line after every level : ")
Tree.printnextlevel(Tree.root)

        
            
