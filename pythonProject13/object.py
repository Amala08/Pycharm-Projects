class BankAccount:
    def __init__(self,name,number,acc_type):
        self.account_name = name
        self.account_number = number
        self.account_type = acc_type
        self.initial_balance = 10000
    def deposit(self,amount):
        print(f"You have deposited ${amount}")
        total_balance = self.initial_balance + amount
        print(f"Your Total Balance is ${total_balance}")
    def withdrawal(self,amount):
        if amount > self.initial_balance:
            print("You do not have sufficient Balance")
            print(f"Your Current Balance is {self.initial_balance}")
        else:
            print(f"You have withdrawn ${amount}")
            total_balance = self.initial_balance - amount
            print(f"Your Total Balance is ${total_balance}")
state_bank = BankAccount("Amala",123455666777,"savings")
state_bank.deposit(2000)
state_bank.withdrawal(15000)
