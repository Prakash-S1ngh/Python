class parent:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print(self):
        print("x== ",self.x)
        print("y== ",self.y)

class child(parent):
    def __init__(self,x,y,a,b):
        super().__init__(x,y)
        self.a=a
        self.b=b
    def print(self):
        print("a==",self.a)
        print("b==",self.b)
x=child(4,5,6,7)
x.print()

#Assignment: does method overloading exist in python
a=5+6
b='5'+'6'
print(a)
print(b)
#Encapsulation:
#Data in methods which can manipulted or acess that data are combined together in one unit  is called encapsulation