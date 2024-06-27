class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def add(self,other):
        self.real=self.real + other.real
        self.img=self.img + other.img
        print(self.real , self.img)
        

c1=complex(3,5)
c2=complex(4,5)
c1.add(c2)
#Assignment=1/2-2/3 and the result is in fraction
    
    