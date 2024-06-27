class node:
     def __init__(self,data):
         self.data = data
         self.left = None
         self.right = None


class tree:
     def __init__(self):
          self.root = None

     def insert(self,data):
          new_node = node(data)
          if self.root is None:
               self.root = new_node
          else:
               curr = self.root
               curr1=curr
               while curr:
                   if curr.data > data:
                       curr1=curr
                       curr = curr.left
                   else:
                       curr1=curr
                       curr = curr.right
               if curr1.data > data:
                    curr1.left = node(data)

               else:
                   curr1.right = node(data)

                   if curr1.data > data:
                        curr1.left = node(data)
                   else:
                        curr1.right = node(data)

     def display(self,root):
          if root is None:
               return 
          print(root.data,end=' -> ')
          self.display(root.left)
          self.display(root.right)
     
     def countheight(self,root):
          if root is None:
               return 0;
          else:
               return max(self.countheight(root.left),self.countheight(root.right))+1
          
     def numberofNodes(self,root):
          if root is None:
               return 0;
          return self.numberofNodes(root.left) + self.numberofNodes(root.right) + 1     

              

Tree = tree()
list = [20,17,23,25,16,10,9]
for i in list:
     Tree.insert(i)

print("the list is ",list)
print("the preordered is : ")
Tree.display(Tree.root)
print('None')
print("height of the tree: ",Tree.countheight(Tree.root))

print("Total number of nodes in tree: ",Tree.numberofNodes(Tree.root))

               
               