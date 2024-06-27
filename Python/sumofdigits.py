a = int(input('Enter 1st number: ')) #User will enter the number
s=0
while a!=0:  #loop iterates till no digits left 
    s+=a%10
    a=a//10
    
print('Sum  is ' ,s) #Result
