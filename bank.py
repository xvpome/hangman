import random
class BankAccount:
    def __init__(self, balance, account_number, owner_name, date_of_open):
        self.balance = balance
        self.account_number = account_number
        self.owner_name = owner_name
        self.date_of_open = date_of_open
    def deposit(self, money):
        self.balance = self.balance + money
        print(f"You deposited {money}$")
    def withdraw(self, money):
        self.balance = self.balance - money
        print(f"You withdrew {money}$")
    def check_balance(self):
        return f"{self.balance}$"
balance = random.randint(100,10000)
account_number = random.randint(10000000, 100000000000)
owner_name = input("Enter your name: ")
month = random.randint(1,12)
day = random.randint(1,30)
year = random.randint(2020,2023)
if month == 2 and day > 28:
    day = 28
date_of_open = str(day) + "/" + str(month) + "/" + str(year)
account = BankAccount(balance, account_number, owner_name, date_of_open)
choice = input("Would you like to continue? ")
state = False
if choice.lower() == "y":
    state = True
while state is True:
    userChoice = int(input("Would you like to: 1 - Check Balance; 2 - Deposit; 3 - Withdraw; 4 - Quit: "))
    if userChoice == 1:
        print(account.check_balance() )
    elif userChoice == 2:
        money = int(input("Enter cash to deposit: "))
        account.deposit(money)
    elif userChoice == 3:
        money = int(input("Enter cash to withdraw: "))
        account.withdraw(money)
    elif userChoice == 4:
        state = False
        break
    else:
        print(f"Balance: {account.balance}$")
        print(f"Account Number: {account.account_number}")
        print(f"Name: {account.owner_name}")
        print(f"Date Of Opening: {account.date_of_open}")





