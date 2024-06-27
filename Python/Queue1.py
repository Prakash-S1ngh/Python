class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        dequeued_item = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        self.size -= 1
        return dequeued_item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.front.data

    def __len__(self):
        return self.size

# Example usage:
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", len(queue))  # Output: 3

print("Front of queue:", queue.peek())  # Output: 1

print("Dequeued item:", queue.dequeue())  # Output: 1
print("Dequeued item:", queue.dequeue())  # Output: 2

print("Queue size after dequeues:", len(queue))  # Output: 1
