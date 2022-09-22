from datetime import datetime

class Bank:
    balance = 0
    
    
    def withdrawal(self):
        withdraw = input("How much you like to withdraw: ")
        currentdatetime = datetime.now()
        if int(withdraw) <= self.balance:
            self.balance = self.balance - int(withdraw)
            with open("transactions.txt", "a") as file:
                file.write(f"You have withdrawn {withdraw} \n Balance: {self.balance} \t\t\t {currentdatetime} \n")
        else:
            print("Insufficient balance")
        

    def Deposit(self):
        deposit = input("How much you like to deposit: ")
        currentdatetime = datetime.now()
        self.balance = self.balance + int(deposit)
        with open("transactions.txt", "a") as file:
            file.write(f"You have deposit {deposit} \n Balance: {self.balance} \t\t\t {currentdatetime} \n")

            

bankingapp = Bank()
while True:
    action = input("Welcome! Please enter d for deposit, w for withdrawal or q to quit: ")

    if action == 'd':
        bankingapp.Deposit()
    elif action == 'w':
        bankingapp.withdrawal()
    elif action == 'q':
        break
    else: 
        print("Wrong Input")