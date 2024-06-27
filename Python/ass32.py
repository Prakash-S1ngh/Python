class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)

# Creating objects of the Person class
person1 = Person("Alex", 30)
person2 = Person("Roshan", 25)

# Accessing object attributes
print(person1.display())  

print(person2.display())   
