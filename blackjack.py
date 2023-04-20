import random

programState = True

while programState == True:
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
            print(f"Your cards were {userCardList})
            print()
            break
        elif computerSum > 21:
            print(f"You win, computer cards were {computerCardList}")
            print(f"Your cards were {userCardList}")
            print()
            break
        elif sumUser == computerSum:
            print(f"You draw, computer cards were {computerCardList}")
            print(f"Your cards were {userCardList}")
            print()
            break
        
        elif sumUser > computerSum:
            print(f"You win, computer cards were {computerCardList}")
            print(f"Your cards were {userCardList}")
            print()
            break
        
        elif sumUser < computerSum:
            print(f"You lose, computer cards were {computerCardList}")
            print(f"Your cards were {userCardList}")
            print()
            break
        
    

    
            

   
                                    
    
    
    
    
    
    
    
    
    
    
