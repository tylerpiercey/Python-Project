import random
import db

#comments
def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

def makeDeck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    pointValues = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append([rank, suit, pointValues[ranks.index(rank)]])
    return deck

def stand(dealerHand, playerTotal, dealerTotal, deck, account, bet):
    dealerHand.append(deck.pop())
    dealerTotal += dealerHand[1][2]
    print("DEALER' CARDS:")
    for i in range(len(dealerHand)):
        while dealerTotal < 17 and dealerTotal < playerTotal:
            dealerHand.append(deck.pop())
            dealerTotal += dealerHand[i + 2][2]
    for i in range(len(dealerHand)):
        print(F"{dealerHand[i][0]} of {dealerHand[i][1]}")
    if dealerTotal > 21 or dealerTotal < playerTotal:
        account += bet
        print()
        print(f"YOUR POINTS: {playerTotal}")
        print(f"DEALER'S POINTS: {dealerTotal}")
        print()
        print("Player wins!")
        print()
        db.write_balance(account)
    elif playerTotal == dealerTotal:
        print("Draw!")
    else:
        account -= bet
        print()
        print(f"YOUR POINTS: {playerTotal}")
        print(f"DEALER'S POINTS: {dealerTotal}")
        print()
        print("Sorry. You lose.")
        db.write_balance(account)

def main():
    account = db.read_balance()
    deck = makeDeck()
    title()
    while True:
        if account < 5:
            choice = input("Not enough in you account would you like to buy more chips (y/n): ")
            if choice.lower() == "y":
                try:
                    amount = float(input("How much would you like to buy: "))
                except ValueError:
                    print("Enter valid input.")
                account += amount
                db.write_balance(account)
            else:
                print("Thanks for playing.")
                break

        playerHand = []
        dealerHand = []

        random.shuffle(deck)

        playerHand.append(deck.pop())
        playerHand.append(deck.pop())

        dealerHand.append(deck.pop())
        try:
            bet = float(input("Make a bet: "))
            if bet < 5 or bet > 1000 or bet > account:
                print("bet must be higher than 5 and less than 1000.")
            else:
                print("DEALER'S SHOW CARD:")
                print(f"{dealerHand[0][0]} of {playerHand[0][1]}")
                print()
                print("YOUR CARDS:")
                print(F"{playerHand[0][0]} of {playerHand[0][1]}")
                print(F"{playerHand[1][0]} of {playerHand[1][1]}")
                print()
                playerTotal = playerHand[0][2] + playerHand[1][2]
                dealerTotal = dealerHand[0][2]
                if playerTotal == 21:
                    print("Blackjack!")
                    account += 1.5 * bet
                    db.write_balance(account)
                    break
                while playerTotal < 22:
                    choice = input("Hit or Stand (hit/stand): ")
                    print()
                    if choice.lower() == "s":
                        stand(dealerHand, playerTotal, dealerTotal, deck, account, bet)
                        break
                    elif choice.lower() == "h":
                        aces = 0
                        playerTotal = 0
                        playerHand.append(deck.pop())
                        print("YOUR CARDS:")
                        for i in range(len(playerHand)):
                            print(F"{playerHand[i][0]} of {playerHand[i][1]}")
                            if playerHand[i][0] == "Ace":
                                aces += 1
                            playerTotal += playerHand[i][2]
                            if playerTotal > 21 and aces > 0:
                                playerTotal -= 10
                                aces -= 1
                        print()
                        print(f"Current score: {playerTotal}")
                        print()
                        if playerTotal > 21:
                            print("sorry. you lose.")
                            print()
                            account -= bet
                            db.write_balance(account)
                    else:
                        print("Invalid Input")
        except ValueError:
            print("Enter valid input.")
            print()
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

if __name__ == "__main__":
    main()