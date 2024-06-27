class ATM():
    def __init__ (self,acc,balance,name):
        self.name=name
        self.balance=balance
        self.acc=acc
    
    def withdraw(self,amount):
        if(amount<self.balance):
          self.balance=self.balance-amount
        else:
            print("Balande insufficient")
    
    def deposit(self,amount):
        self.balance=self.balance+amount

    def display(self):
        print(f"the Account num: ",self.acc)
        print(f"The account holder:",self.name)
        print(f"the balance remaining is : ",self.balance)

    def trans(self):
     while True:
        t = int(input("Enter the choice"))
        if t == 1:
            maal = int(input("Enter the amount: "))
            atm.withdraw(maal)
        elif t == 2:
            bal = int(input('Enter the amount: '))
            atm.deposit(bal)
        elif t==3:
            atm.display()
        else:
            break

            

name=input("Enter the name: ")
acc=input('Enter the account number: ')
bal=int(input('Enter the balance: '))
atm=ATM(acc,bal,name)
atm.trans()