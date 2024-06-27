
# Online Python - IDE, Editor, Compiler, Interpreter


a = int(input('Enter 1st number: ')) #User will enter the number.
f=1
s=0
k=a
while a!=0: # loop for every digit
    b=a%10
    f=1
    while(b!=0): #loop for factorial of every digit
        f=f*b
        b=b-1
    s=s+f
    a=a//10
if s==k:
    print('Yes')
else :
    print('No')

    


