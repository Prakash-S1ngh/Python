from functools import reduce
# l=[1,2,34,5,6,7,8]
# cube=lambda x: x*x*x
# newl=[]
# for item in l:
#     newl.append(cube(item))

# print(newl)

#or



# cube=lambda x: x*x*x
# l=[1,2,3,4,5,6,7]
# newl=list(map(cube,l))
# print(newl)



# Using filter 
def fil_func(a):
    return a>50

l=[34,56,89,90,45]
newlist=list(filter(fil_func,l))
print("Without filter: ",l)
print("With using filter: ",newlist)

#reduce function
def sum(x,y):
    return x+y

ne=reduce(sum,l)
print("Using reduce function : ",ne)