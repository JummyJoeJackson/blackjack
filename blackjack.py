#imports random function
from random import randrange

#declares global variables
cardSuits = ["Spades","Clubs","Diamonds","Hearts"]
cardValues = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace",]
user_hand = []
comp_hand = []
user_hand_val = 0
comp_hand_val = 0

#defines hit function that gives user random card
def hit(player):
    card = cardValues[randrange(0,12)] + " of " + cardSuits[randrange(0,3)]
    player.append(card)

#defines function to give user their hand
def starting_cards():
    for i in range(2):
        hit(user_hand)
    print("Your hand is " + user_hand[0] + " and " + user_hand[1])

#defines function to check user's card's value
def check_card_val(position, player):
    global user_hand_val
    global comp_hand_val
    for i in range(9):
        if str(i + 2) in player[position]:
            user_hand_val = user_hand_val + (i + 2)
            print("This user's first card is worth " + str(i + 2))
            break
    if "Jack" in player[position]:
        user_hand_val = user_hand_val + 10
        print("This user's first card is worth 10")
    elif "Queen" in player[position]:
        user_hand_val = user_hand_val + 10
        print("This user's first card is worth 10")
    elif "King" in player[position]:
        user_hand_val = user_hand_val + 10
        print("This user's first card is worth 10")
    elif "Ace" in player[position]:
        user_hand_val = user_hand_val + 11
        print("This user's first card is worth 11")

#defines function to check and print user's total hand value
def check_hand_val():
    if user_hand_val == 21:
        print("YOU GOT A BLACKJACK!")
    elif user_hand_val > 21:
        print("YOU BUSTED!")
        print("YOUR HAND IS WORTH " + str(user_hand_val))
    elif user_hand_val < 21:
        print("YOUR HAND IS WORTH " + str(user_hand_val))

#executes commands
starting_cards()
check_card_val(0, user_hand)
check_card_val(1, user_hand)
check_hand_val()
