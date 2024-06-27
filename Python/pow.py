#user inputs 
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
s=1
while b!=0: #loop iterates till b=0
    s*=a
    b=b-1
    

print(f'Pow of {a} and {b}',s)
