#imports random function
from random import randrange

#declares constant for the different card suits
CARD_SUITS = ["Spades","Clubs","Diamonds","Hearts"]
#declares constant for the diffenet card names
CARD_NAMES = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace",]
#declares dictionary for the values of each card
CARD_VALUES_MAP = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}
#declares global variables
user = []
comp = []
user_val = 0
comp_val = 0
player_val = 0

#defines hit function that gives user random card
def hit(player):
    #creates a random card
    card = f"{CARD_NAMES[randrange(0,12)]} of {CARD_SUITS[randrange(0,3)]}"
    #could also use f"{CARD_NAMES[randrange(len(CARD_NAMES))]} of {CARD_SUITS[randrange(len(CARD_SUITS))]}" if more cards are added
    #adds that card to the array player (user or comp)
    player.append(card)

#defines function to give user their hand
def give_cards(player):
    #gives two cards to player (user or comp)
    for i in range(2):
        hit(player)
    #prints the hand of the player
    print(f"Your hand is {player[0]} and {player[1]}")

#defines function to check user's card's value
def check_card_val(position, player):
    #declares global variables so that function can change them
    global player_val
    global user_val
    global comp_val
    #finds card name
    card = player[position].split()[0]
    #adds the card value to player value
    player_val += CARD_VALUES_MAP[card]
    #checks if the player is the user
    if player == user:
        #checks if it's the first card
        if position == 0:
            #makes user value the same as player value
            user_val = player_val
            #prints how much the user's first card is worth
            print(f"The user's first card is worth {user_val}")
        #checks if it's the second card
        elif position == 1:
            #checks how much the second card is worth by subtracting the first card's value from player value and then makes that the user value
            user_val = player_val - user_val
            #prints how much the user's first card is worth
            print(f"The user's second card is worth {user_val}")
    #checks if the player is the computer
    elif player == comp:
        #checks if it's the first card
        if position == 0:
            #makes computer value the same as player value
            comp_val = player_val
            #prints how much the computer's first card is worth
            print(f"The computer's first card is worth {comp_val}")
        #checks if it's the second card
        elif position == 1:
            #checks how much the second card is worth by subtracting the first card's value from player value and then makes that the computer value
            comp_val = player_val - comp_val
            #prints how much the computer's second card is worth
            print(f"This computer's second card is worth {comp_val}")

#defines function to check if user has blackjack
def check_blackjack():
    #checks if player value is 21
    if player_val == 21:
        print("YOU GOT A BLACKJACK!")

#defines function to check if user busted
def check_bust():
    #checks if player value is greater than 21
    if player_val > 21:
        print("YOU BUSTED!")
        print(f"YOUR HAND IS WORTH {player_val}")

#defines function to check and print user's hand value
def check_hand_val():
    #checks if player got blackjack
    check_blackjack()
    #checks if player busted
    check_bust()
    #checks if player value is lower than 21
    if player_val < 21:
        print(f"YOUR HAND IS WORTH {player_val}")

#executes commands
give_cards(user)
check_card_val(0, user)
check_card_val(1, user)
check_hand_val()
