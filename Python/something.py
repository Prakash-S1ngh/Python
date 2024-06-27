class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
       
    
    def insert(self, data):
        new_node = Node(data)
        if  self.head is None:
            self.head = new_node
            
        else:
            tail = self.head
            while tail.next:
               tail =tail.next
            tail.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def printrev(self):
        def rev(root):
            if root is None:
                return 
            rev(root.next)
            print(root.data , end="->1")

        rev(self.head)
        print("None")

# list=[12,13,14,15,16]
        
lst=[]
for i in range(0,5):
    ele=int(input())
    lst.append(ele)

linked_list = LinkedList()
for num in lst:
    linked_list.insert(num)
print(lst)
print("Linked List:")
linked_list.display()
print()
linked_list.printrev()
