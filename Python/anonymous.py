double=lambda x: x**x
def fun(fx,value):
    return 200+fx(value)
y=int(input("Enter the number"))

print(double(y))
#passing function to function
print(fun(double,y))
