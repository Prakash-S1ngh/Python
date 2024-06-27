class GHAR:
    def __init__ (self,name,street):
        self.name=name
        self.street=street
   
    def display(self):
       
        print(f"The house holder:",self.name)
        print(f"the street name : ",self.street)

    

g=GHAR("Ram","Bhopal")
g.display()