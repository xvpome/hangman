from replit import clear

state = True
bids = {"names" : [], "bids": []}
bidsList = list(bids["bids"])
namesList = bids["names"]
while state:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidsList.append(bid)
    namesList.append(name)
    choice = input("Are there any other bidders? 'yes' or 'no'\n")
    if choice.lower() == "yes":
        clear()
    elif choice.lower() == "no":
        state = False
        break
index = bidsList.index(max(bidsList))
print(f"Winner is {namesList[index].title()} with a bid of ${bidsList[index]}")





    
