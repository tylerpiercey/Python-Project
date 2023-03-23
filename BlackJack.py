# create a list to store suit rank and point value

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
pointValues = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]

deck = []

for suit in suits:
    for rank in ranks:
        deck.append([rank, suit, pointValues[ranks.index(rank)]])
print(deck)

