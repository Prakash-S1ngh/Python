class ATM:
    def __init__(self , Acc , Amount , Password):
        self.Acc_No = Acc
        self.__Amount = Amount                      #This makes the Amount and Password to be accessed in class only and are private 

        self.__Password = Password

    def get_info(self):                             #getter method
        return self.__Amount
    
    def withdraw(self , Amnt):                      #setter method 
        self.__Amount = self.__Amount - Amnt


My_bank = ATM(1021 , 10000 , 5342)
My_bank.withdraw(1200)
print(My_bank.Acc_No)
print(My_bank.get_info())
    
