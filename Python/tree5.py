class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def display(self, root):
        if root is None:
            return 
        print(root.data, end=' -> ')
        self.display(root.left)
        self.display(root.right)

    def createBinary(self, inorder, pre):
        preInd = 0

        def create(inorder, pre, start, end):
            nonlocal preInd
            if start > end:
                return None
            if preInd >= len(pre):
                return None
            
            root = node(pre[preInd])
            preInd += 1
            index = 0 

            for i in range(start, end + 1):
                if inorder[i] == root.data:
                    index = i
                    break
            root.left = create(inorder, pre, start, index - 1)
            root.right = create(inorder, pre, index + 1, end)
            return root

        return create(inorder, pre, 0, len(pre) - 1)

    def serialised(self, root):
        list1 = []

        def startserial(root, list1):
            if root is None:
                list1.append(-1)
                return list1

            list1.append(root.data)
            startserial(root.left, list1)
            startserial(root.right, list1)

            return list1

        return startserial(root, list1)
    

    def desirialised(self, list2):
        preIndex = 0

        def chalukredesirialised(list2, preIndex):
            if list2[preIndex] == -1:
                return None
            if preIndex == len(list2):
                return None

            Node = node(list2[preIndex])  # Corrected the assignment
            preIndex = preIndex + 1
            Node.left = chalukredesirialised(list2, preIndex)  # Added missing arguments
            Node.right = chalukredesirialised(list2, preIndex)  # Added missing arguments

            return Node

        return chalukredesirialised(list2, preIndex)  # Corrected indentation


inorder = [4, 2, 5, 1, 6, 3, 7]
pre = [1, 2, 4, 5, 3, 6, 7]
Tree = tree()
Tree.root = Tree.createBinary(inorder, pre)
print("The tree created is:")
Tree.display(Tree.root)
print()
# serialising the tree 
serial = Tree.serialised(Tree.root)
print(serial)

deserialized_tree = Tree.desirialised(serial)
print("The deserialized tree is:")
Tree.display(deserialized_tree)

