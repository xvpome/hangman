import random

def program():
    
    state = True
    priceLatte = 250
    priceCappucino = 300
    priceEspresso = 150

    water = random.randint(300, 1000)
    milk = random.randint(300, 500)
    coffee = random.randint(100, 300)

    money = 0

    class Pay:
        
        dime = 0
        nickel = 0
        quarter = 0
        penny = 0

        def payment(self, quarters, dimes, nickels, pennies, sum = 0):
            sum = sum + (quarters*25)
            sum = sum + (dimes*10)
            sum = sum + (nickels*5)
            sum = sum + (pennies*1)
            return sum

    while state:
        
        mainObject = Pay()
        dime = mainObject.dime
        quarters = mainObject.quarter
        nickel = mainObject.nickel
        penny = mainObject.penny

        
        
        choice = input("What would you like? (espresso/latte/cappucino): ")

        if choice.lower() == "report":

            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: {(money)/100}$")

        elif choice.lower() == "espresso":
            if water < 50:
                print("Not enough water")
            elif coffee < 18:
                print("Not enough coffee")
            elif coffee < 18 and water < 50:
                print("Not enough coffee and water")
                
            else:
                
                water = water - 50
                coffee = coffee - 18
                quarters = int(input("How many quarters: "))
                dime = int(input("How many dimes: "))
                nickel = int(input("How many nickel: "))
                penny = int(input("How many pennies: "))
                sum = mainObject.payment(quarters, dime, nickel, penny)
                if sum > priceEspresso:
                    print(f"Here is {(sum - priceEspresso)/100}$ change")
                    print("Here is your espresso. Enjoy!")
                    money = money + priceEspresso
                elif sum == priceEspresso:
                    print("Here is your espresso. Enjoy!")
                    money = money + priceEspresso
                else:
                    print("Not enough money. Money Refunded")

        elif choice.lower() == "latte":
            
            if water < 200:
                print("Not enough water")
            elif coffee < 24:
                print("Not enough coffee")
            elif coffee < 24 and water < 200:
                print("Not enough coffee and water")
            elif milk < 150:
                print("Not enough milk")
            elif milk < 150 and coffee < 24:
                print("Not enough milk and coffee")
            elif milk < 150 and water < 200:
                print("Not enough milk and water")
            elif milk < 150 and coffee < 24 and water < 200:
                print("Not enough milk and coffee and water")
                
            else:
                milk = milk - 150
                water = water - 200
                coffee = coffee - 24
                quarters = int(input("How many quarters: "))
                dime = int(input("How many dimes: "))
                nickel = int(input("How many nickel: "))
                penny = int(input("How many pennies: "))
                sum = mainObject.payment(quarters, dime, nickel, penny)
                if sum > priceLatte:
                    print(f"Here is {(sum - priceLatte)/100}$ change")
                    print("Here is your latte. Enjoy!")
                    money = money + priceLatte
                elif sum == priceLatte:
                    print("Here is your latte. Enjoy!")
                    money = money + priceLatte
                else:
                    print("Not enough money. Money Refunded")

        elif choice.lower() == "cappuccino":
            
            if water < 250:
                print("Not enough water")
            elif coffee < 24:
                print("Not enough coffee")
            elif coffee < 24 and water < 250:
                print("Not enough coffee and water")
            elif milk < 100:
                print("Not enough milk")
            elif milk < 100 and coffee < 24:
                print("Not enough milk and coffee")
            elif milk < 100 and water < 250:
                print("Not enough milk and water")
            elif milk < 100 and coffee < 24 and water < 250:
                print("Not enough milk and coffee and water")
                
            else:
                
                milk = milk - 100
                water = water - 250
                coffee = coffee - 24
                quarters = int(input("How many quarters: "))
                dime = int(input("How many dimes: "))
                nickel = int(input("How many nickel: "))
                penny = int(input("How many pennies: "))
                sum = mainObject.payment(quarters, dime, nickel, penny)
                if sum > priceCappucino:
                    print(f"Here is {(sum - priceCappucino)/100}$ change")
                    print("Here is your cappucino. Enjoy!")
                    money = money + priceCappucino
                elif sum == priceCappucino:
                    print("Here is your cappucino. Enjoy!")
                    money = money + priceCappucino
                else:
                    print("Not enough money. Money Refunded")

        elif choice.lower() == "quit":
            state = False
            break   
        
program()     
