import random

# create a list to store suit rank and point value

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
pointValues = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]

deck = []

for suit in suits:
    for rank in ranks:
        deck.append([rank, suit, pointValues[ranks.index(rank)]])

playerHand = []
dealerHand = []

random.shuffle(deck)

playerHand.append(deck.pop())
playerHand.append(deck.pop())
#print(playerHand)

dealerHand.append(deck.pop())
dealerHand.append(deck.pop())
#print(dealerHand)

print("DEALER'S SHOW CARD:")
print(f"{dealerHand[0][0]} of {playerHand[0][1]}")
print()
print("YOUR CARDS:")
print(F"{playerHand[0][0]} of {playerHand[0][1]}")
print(F"{playerHand[1][0]} of {playerHand[1][1]}")
playerTotal = 0
dealerTotal = 0

while True:

    choice = input("Hit or Stand (hit/stand): ")
    if choice.lower() == "stand":

        print("DEALER' CARDS:")
        for i in range(len(dealerHand)):
            print(F"{dealerHand[i][0]} of {dealerHand[i][1]}")
        print()
        break
    elif choice.lower() == "hit":
        playerHand.append(deck.pop())

        print("YOUR CARDS:")
        for i in range(len(playerHand)):
            print(F"{playerHand[i][0]} of {playerHand[i][1]}")
            playerTotal += playerHand[i][2]
        if playerTotal > 21:
            print("sorry. you lose.")
            break
    else:
        print("Invalid Input")




