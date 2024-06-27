class atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        print(id(self.balance))
        self.menu()
    def menu(self):
        user_input= input('''How would you like to proceed?
                            1. Enter 1 to create pin
                            2. Enter 2 to deposit
                            3. Enter 3 to withdrwal
                            4. Enter 4 to check balance
                            5. enter 5 to exist ''')
        if user_input=="1":
            #print("Create pin")
            self.create_pin()
            print("Pin Successfully")
            self.menu()
        elif user_input=="2":
            
            self.deposit()
            print("Deposit")
        elif user_input=="3":
            self.withdrwal()
        elif user_input=="4":
            self.check_balance()
        elif user_input=="5":
            print("Exist")
    def create_pin(self):
        self.pin=input("Enter Pin ")
    def deposit(self):
        temp=input("Enter your Pin")
        if temp==self.pin:
            amount=int(input("Enter amount"))
            #id(amount)
            self.balance=self.balance+amount
            print("Deposit Successful")
        else:
            print("Invild Pin")
    def withdrwal(self):
        temp=input("Enter Pin")
        if temp==self.pin:
            amount=int(input("Enter amount"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Operation successful")
            else:
                print("Insufficient Funds")
        else:
            print("Invild Pin")
    def check_balance(self):
        temp=input("Enter Pin ")
        if temp==self.pin:
            print(self.balance)
        else:
            print("invalid pin")
        self.menu()

    


a=atm()
a.menu()
