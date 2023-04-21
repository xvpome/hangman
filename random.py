import random
randomNumber = random.randint(1,100)
state = True
tries = 0
while state is True:
    guess = input("Guess the number ")
    tries += 1
    if guess > randomNumber:
        print("lower")
    elif guess < randomNumber:
        print("Higher")
    else:
        state = False
        break
print(f"The number was {randomNumber}, it took you {tries} tries!")
