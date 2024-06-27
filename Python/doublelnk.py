# this to declare and initialise node

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


# this to declare and initialise double linkList's head and tail

class dlinklist:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert(self,data):
        new_node = node(data)

        if self.head is None:
            self.head=new_node
            self.tail = new_node


        else:
            current=self.head
            while current.next is not  None:
                current = current.next
            current.next = new_node
            new_node.prev = current


    def printllist(self):
          current=self.head
          while current is not None:
                if(current.next is None):
                    self.tail = current
                print(current.data, end=" -> ")
                current = current.next



    def printreverse(self):
          current=self.tail
          while current is not None:
                print(current.data, end=" <- ")
                current = current.prev
        



list = [12,13,14,15,16]
double = dlinklist()

for i in list:
    double.insert(i)

print("list is : ",list)
print("Double linkList is : ",end=' ')
double.printllist()
print(" Reversed Double linkList is : ")
double.printreverse()


            