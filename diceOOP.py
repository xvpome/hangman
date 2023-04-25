import random

class Random():
    def dice(self):
        return (random.randint(1,6))

obj = Random()
state = False
choice = input("Would you like to roll the dice?: ")
if choice.lower() == "yes":
    state = True
    
while state is True:
    
    choice = input("Would you like to roll the dice?: ")
    if choice.lower() == "yes":
        number = obj.dice()
        print(f"Your got the number {number}")
        
    else:
        state = False
        break
    
