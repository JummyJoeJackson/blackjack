#importing functions
import random

#assign all possible card suits and values
cardSuits = ["Spades","Clubs","Diamonds","Hearts"]
cardValues = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King',"Ace",]
user_card = ""

#function for assigning user a card
def first_card():
	user_card = str(cardValues[randrange(0,12)]) + " of " + str(cardSuits[randrange(0,3)])
			  
first_card()
print(user_card)
