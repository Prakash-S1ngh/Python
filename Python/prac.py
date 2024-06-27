class Teacher:
    def __init__(self):
      self.name="Prakash"
      self.age="23"
      print(id(self))

    def display(self):
        print(self.name)
        print(self.age)

t1=Teacher()
t1.display()
print(id(t1))
# t2=Teacher()
# #self refer to current object inside the class
# # static variable (clss level value) the value is same for all the object
# class Teacher:

#     instructor="manit vareable" # static variable
#     def __init__(self):


# there are three types of method 
# 1.Instance method: instance variable jaha pe aayenge usko instance method bolenge
# 2.inside any two method only class variable for example
# for every class class level object are created by pvm(python virtual machine to store class related information)
class Teacher:
   @classmethod
   def fun(cls):
      print(id(cls))
print(Teacher.fun())
print(Teacher.fun())
#use of OOPS :
#1.to use user defined datatype
#2.

# class complex:
#    def __init__(self,real ,img):
#       self.real=real
#       self.img=img
         
      
