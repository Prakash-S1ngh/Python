class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def construct_binary_tree(elements):
    if not elements:
        return None
    root = TreeNode(elements[0])
    for value in elements[1:]:
        insert(root, value)
    return root

def inorder_traversal(root):
    if root:
        print(root.value, end=" ")
        inorder_traversal(root.left)
        inorder_traversal(root.right)

def findpth(root , path , n):
    if root is None:
        return None
    path.append(root)
    if root.value == n:
        return True
    if (findpth(root.left , path , n) or findpth(root.right ,  path , n)):
        return True
    path.remove(root)
    return False
    
    

def printspiral(root ,n1 , n2 ):
    l1 = []
    l2 = []
    if root is None:
        return None
    if( findpth(root.left , l1 , n1) and findpth(root.right , l2 , n2)):
        return None
       
    i =0
    while(i<len(l1) and i<len(l2)):
        if l1[i] != l2[i]:
            break
        i+=1

    return l1[i-1]

def zigzag_level_traversal(root):
    if root is None:
        return []

    result = []
    queue = [root]
    left_to_right = True

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.pop(0)

            # Process node
            current_level.append(node.value)

            # Add child nodes to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            current_level.reverse()

        result.extend(current_level)
        left_to_right = not left_to_right

    return result

# Test the function





        


        
    

# Given list of elements
elements = [40, 20, 70, 10, 30, 60, 80, 5, 15, 25, 35, 55, 65, 75, 85]


# Construct binary tree
root = construct_binary_tree(elements)

# Perform inorder traversal to verify the tree
print("Inorder Traversal:")
inorder_traversal(root)
print()

# l1=[]
# l2=[]
# n1=15 
# n2 = 30
# r= printspiral(root , 15 , 30)
# print(r.value)
 
result = zigzag_level_traversal(root)
print(result)