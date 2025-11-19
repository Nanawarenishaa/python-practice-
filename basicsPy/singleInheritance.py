class bankAccount:
    def __init__(self,balance):
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount
        print(f"Deposite amount: Rs.{amount} | Balance in account After deposite: Rs.{self.balance}")

class savingAccount(bankAccount):
    def AddInterest(self):
        interest= self.balance*0.05
        self.balance+=interest
        print(f"Added interest: Rs.{interest} | Now Balance in account: Rs.{self.balance} ")

SA=savingAccount(50000)
SA.deposite(4000)
SA.AddInterest()