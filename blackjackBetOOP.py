import random

class BankAccount:
    
    def __init__(self, balance, account_number, date_of_open, bet = 0):
        
        self.bet = bet
        self.balance = balance
        self.account_number = account_number
        self.date_of_open = date_of_open
        
    def check_balance(self):
        return f"{self.balance}$"
    
    def bet_money(self):
        
        money_state = True
        
        while money_state is True:
            
            money = int(input("Enter money to bet: "))
            
            if money > self.balance:
                print("You don't have enough money in your balance ")
                
                choiceInfo = input("Would you like to check your account info? ")
                
                if choiceInfo.lower() == "yes" or choiceInfo.lower() == "y":
                    print(f"Balance {account.balance}$")
                    print(f"IBAN {account.account_number}")
                    print(f"Date of opening {account.date_of_open}")
                
            elif money == 0:
                
                print("You can't bet 0$!")
                
            else:
                
                bet = self.bet + money
                self.balance = self.balance - money
                print(f"Sucessfully bet {money}.")
                print(f"Bet is now {bet}$")
                print(f"Remaining money {self.balance}$")
                self.bet = bet
                money_state = False
                break
            


profit = 0
balance = random.randint(100,10000)
account_number = random.randint(10000000, 100000000000)
month = random.randint(1,12)
day = random.randint(1,30)
year = random.randint(2020,2023)

if month == 2 and day > 28:
    day = 28
    
date_of_open = str(day) + "/" + str(month) + "/" + str(year)
account = BankAccount(balance, account_number, date_of_open)

programState = True

while programState == True:

    if profit < 0:
        print(f"You have lost {profit}$")
        
    elif profit > 0:
        print(f"You are in a profit of {profit}$")
        
    else:
        print("You haven't made or lost any money! ")

    state = False
    cardPoints = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    computerDraw = ['yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no']

    pointsList = list(cardPoints) 
    answer = input("Do you wanna play a game of BlackJack? ")

    if answer.lower() == "yes":
        state = True
        
    elif answer.lower() == "no":
        programState = False
        break

    while state:

        
        randomCard = 0
        randomCardComputer = 0
        sumUser = 0
        computerSum = 0
        
        userCardOne = random.choice(cardPoints)
        userCardTwo = random.choice(cardPoints)
        userCardList = [userCardOne, userCardTwo]
    
        computerCardOne = random.choice(cardPoints)
        computerCardTwo = random.choice(cardPoints)
        computerCardList = [computerCardOne, computerCardTwo]
        
      
        print(f"Your cards are {userCardList} ")
        print(f"Computer's first card is {computerCardList[0]}")
        print()

        betChoice = input("Do you want to bet? ")

        if betChoice.lower() == "yes" or betChoice.lower() == "y":
            bet_state = True
            while bet_state:
                choice = input("Do you wanna bet? ")
                if choice.lower() == "no":
                    bet_state = False
                    break
                account.bet_money()
             
        print()
            
        userDrawAnother = input("Type 'yes' to get another card, type 'no' to pass it: ")
        print()
        if userDrawAnother.lower() == 'yes':
            drawAnotherCard = True
            
            while drawAnotherCard:
                randomCard = random.choice(cardPoints)
                userCardList.append(randomCard)
                
                print()
                
                userDrawAnother = input("Type 'yes' to get another card, type 'n' to pass it: ")
                print(userCardList)
                if userDrawAnother.lower() == 'no':
                    drawAnotherCard = False
                    break
        
        computerChoice = random.choice(computerDraw)
        
        if computerChoice == 'yes':
            drawComputer = True
            while drawComputer is True:
                
                randomCardComputer = random.choice(cardPoints)
                print(f"Computer drew {randomCardComputer}")
                computerCardList.append(randomCardComputer)
                
                if computerChoice.lower() == 'no':
                    drawComputer = False
                    break
                
        for x in userCardList:
            sumUser = sumUser + x
        for x in computerCardList:
            computerSum = computerSum + x
        
        if sumUser > 21:
            print(f"You lose, computer cards were {computerCardList}")
            profit = profit - account.bet
            print(f"Your cards were {userCardList}")
            print()
            break
        elif computerSum > 21:
            print(f"You win, computer cards were {computerCardList}")
            profit = profit + account.bet
            print(f"Your cards were {userCardList}")
            print(f"You win {account.bet * 2}$.")
            account.balance = account.balance + (account.bet * 2)
            print(f"Your balance is now {account.balance}")
            print()
            break
        elif sumUser == computerSum:
            print(f"You draw, computer cards were {computerCardList}")
            print(f"Your cards were {userCardList}")
            print()
            break
        
        elif sumUser > computerSum:
            profit = profit + account.bet
            print(f"You win {account.bet * 2}$.")
            win = win + account.bet
            account.balance = account.balance + (account.bet * 2)
            print(f"Your balance is now {account.balance}")
            print(f"You win, computer cards were {computerCardList}")
            print(f"Your cards were {userCardList}")
            print()
            break
        
        elif sumUser < computerSum:
            profit = profit - account.bet
            print(f"You lose, computer cards were {computerCardList}")
            print(f"Your cards were {userCardList}")
            print()
            break
            
    if account.balance == 0:
        print(f"You can play anymore you balance is {account.balance}$")
        programState = False
        break

