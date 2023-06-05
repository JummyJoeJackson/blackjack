#imports random function
from random import randrange

#declares global variables
cardSuits = ["Spades","Clubs","Diamonds","Hearts"]
cardValues = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace",]
user_hand = []

#defines hit function
def hit():
    user_card = cardValues[randrange(0,12)] + " of " + cardSuits[randrange(0,3)]
    user_hand.append(user_card)

#executes hit funciton to give user their hand
for i in range(2):
    hit()
print("Your hand is " + user_hand[0] + " and " + user_hand[1])
