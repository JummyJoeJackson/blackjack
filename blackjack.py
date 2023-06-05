#importing functions
from random import randrange

#assign all possible card suits and values
cardSuits = ["Spades","Clubs","Diamonds","Hearts"]
cardValues = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace",]

#gives user a random card
user_card = cardValues[randrange(0,12)] + " of " + cardSuits[randrange(0,3)]
print(user_card)
