class ATM:
    def __init__(self,balance):
        self. __balance = balance
        
    def deposit(self , amount):
        self. __balance += 1000
        print(f"Balance is {self. __balance}")
    def withdraw(self , amount):
        if amount <= self. __balance:
            self. __balance -= amount
            print(f"current balance is {self. __balance }")
        else:
            print("Insuffient balance")
atm = ATM(500)
atm.deposit(10000)
atm.withdraw(500)

        
