import random

# create a list to store suit rank and point value

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
pointValues = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]

deck = []

for suit in suits:
    for rank in ranks:
        deck.append([rank, suit, pointValues[ranks.index(rank)]])

while True:
    playerHand = []
    dealerHand = []

    random.shuffle(deck)

    playerHand.append(deck.pop())
    playerHand.append(deck.pop())


    dealerHand.append(deck.pop())


    print("DEALER'S SHOW CARD:")
    print(f"{dealerHand[0][0]} of {playerHand[0][1]}")
    print()
    print("YOUR CARDS:")
    print(F"{playerHand[0][0]} of {playerHand[0][1]}")
    print(F"{playerHand[1][0]} of {playerHand[1][1]}")
    playerTotal = playerHand[0][2] + playerHand[1][2]
    dealerTotal = dealerHand[0][2]


    while playerTotal < 22:
        choice = input("Hit or Stand (hit/stand): ")
        print()
        if choice.lower() == "s":
            dealerHand.append(deck.pop())
            dealerTotal += dealerHand[1][2]
            #if dealerTotal == 21 and playerTotal == 21:
            print("DEALER' CARDS:")
            for i in range(len(dealerHand)):
                while dealerTotal < 17:
                    dealerHand.append(deck.pop())
                    dealerTotal += dealerHand[i+2][2]
            for i in range(len(dealerHand)):
                print(F"{dealerHand[i][0]} of {dealerHand[i][1]}")
            if dealerTotal > 21 or dealerTotal < playerTotal:
                print()
                print("Player wins!")
                print()
            elif playerTotal == dealerTotal:
                print("Draw!")
            else:
                print("Sorry. You lose.")
                print()
            print(f"YOUR POINTS: {playerTotal}")
            print(f"DEALER'S POINTS: {dealerTotal}")
            print()
            break
        elif choice.lower() == "h":
            playerTotal = 0
            playerHand.append(deck.pop())
            print("YOUR CARDS:")
            for i in range(len(playerHand)):
                print(F"{playerHand[i][0]} of {playerHand[i][1]}")
                playerTotal += playerHand[i][2]
            print(playerTotal)
            if playerTotal > 21:
                print("sorry. you lose.")
                print(playerTotal)
        else:
            print("Invalid Input")
    playAgain = input("Play again (y/n): ")
    print()
    if playAgain.lower() == "n":
        print("Come back soon!")
        print("Bye!")
        break
    elif playAgain.lower() == "y":
        continue
    else:
        print("invalid input. Closing program")
        break




