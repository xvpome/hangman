import random as r
import re

words = ["bettle", "carbon", "diamond", "hangman", "iron", "hearths", "constitution", "spaces", "spade", "dog",
         "dollar", "rich", "cryptonite", "clown"]
word = r.choice(words)
lives = 6
state = True
copy = word
countPrint = 0
for x in word:
    copy = copy.replace(x, "_")
print(word)
while state:

    copy = list(copy)
    print("".join(copy))
    guess = input("Enter a letter or a word: ")

    if guess not in word :
        lives -= 1
        print(f"Wrong guess you have {lives} left. ")

    elif guess in word:
        indexes = [i.start() for i in re.finditer(guess, word)]
        for x in indexes:
            copy[x] = guess
    if guess == word:
        print(f"Congratulations you've won, the word was {word}")
        countPrint = 1
        copy.clear()

    if "_" not in copy and lives != 0 and countPrint == 0:
        state = False
        print(f"Congratulations you've won, the word was {word}")
        state = False
        copy.clear()
    if lives == 0:
        print("You've lost")
        state = False
        copy.clear()



