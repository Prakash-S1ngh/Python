class human:
    def __init__(self,heart , nose):
        self.heart = heart
        self.nose = nose 
        
    def work(self):
        print("I code for myself")
        
        
class Male:
    def __init__(self,eyes):
        self.eye = eyes

    def work(self):
        print("I am the programmer here")

class boy(human , Male):
    def __init__(self, heart, nose , eyes):
        human.__init__(self , heart, nose)
        Male.__init__(self , eyes)

    

boy_1 = boy(1 , 1, "hello")
# Male.work(boy_1)                # use to access work from male without changing the order of passing the clsses order
boy_1.work()
print(boy_1.nose , boy_1.eye , boy_1.heart)



# inheritance are of 4 types"
# 1. single level
# 2. Multilevel inheritance 
# 3. multiple inheritance 
# 4. Hirarchical inheritance
# 5. Hybrid inheritance 
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"MyClass instance with value: {self.value}"

# Creating an instance of MyClass
obj = MyClass(42)

# Printing the object
print(obj)  # Output: MyClass instance with value: 42
