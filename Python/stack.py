class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.data

    def __len__(self):
        return self.size

# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", len(stack))  # Output: 3

print("Top of stack:", stack.peek())  # Output: 3

print("Popped item:", stack.pop())  # Output: 3
print("Popped item:", stack.pop())  # Output: 2

print("Stack size after pops:", len(stack))  # Output: 1
