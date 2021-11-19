#BankAccount class
class BankAccount:
    #Initializer that takes owner's name and balance as the parameter
    def __init__(self,owner_name,balance):
        self.name=owner_name
        self.balance=balance
    #returns owner's name
    def get_name(self):
        return self.name
    #returns balance
    def get_balance(self):
        return self.balance
    #changes owner's name
    def set_name(self,newName):
        self.name=newName
    #changes balance
    def set_balance(self,newBalance):
        self.balance=newBalance
    #prints out bank account summary
    def __str__(self):
        return ("\nBelow is the account info including the updated account balance:"\
               "\nAccount owner:\n"+str(self.get_name())+"\n\nAccount balance:\n"\
                +"$"+str(format(self.get_balance(),'.2f')))
    #adds amount to balance when depositing
    def deposit(self,amount):
        self.balance=self.balance+amount
    #subtracts amount from balance when withdrawing
    def withdraw(self,amount):
        if (self.balance>=amount):
            self.balance=self.balance-amount
        else:
            return "Amount is greater than balance"
    
