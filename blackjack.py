#imports random function
from random import randrange

#declares global variables
CARD_SUITS = ["Spades","Clubs","Diamonds","Hearts"]
CARD_NAMES = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace",]
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
user = []
comp = []
user_val = 0
comp_val = 0
player_val = 0

#defines hit function that gives user random card
def hit(player):
    card = f"{CARD_NAMES[randrange(0,12)]} of {CARD_SUITS[randrange(0,3)]}"
    player.append(card)

#defines function to give user their hand
def give_cards(player):
    for i in range(2):
        hit(player)
    print(f"Your hand is {player[0]} and {player[1]}")

#defines function to check user's card's value
def check_card_val(position, player):
    global user_val
    global comp_val
    global player_val
    card = player[position].split()[0]
    player_val += CARD_VALUES_MAP[card]
    if player == user:
        if position == 0:
            user_val = player_val
            print(f"The user's first card is worth {user_val}")
        elif position == 1:
            user_val = player_val - user_val
            print(f"The user's second card is worth {user_val}")
    elif player == comp:
        if position == 0:
            comp_val = player_val
            print(f"The computer's first card is worth {comp_val}")
        elif position == 1:
            comp_val = player_val - comp_val
            print(f"This computer's second card is worth {comp_val}")

#defines function to check if user has blackjack
def check_blackjack():
    if player_val == 21:
        print("YOU GOT A BLACKJACK!")

#defines function to check if user busted
def check_bust():
    if player_val > 21:
        print("YOU BUSTED!")
        print(f"YOUR HAND IS WORTH {player_val}")

#defines function to check and print user's hand value
def check_hand_val():
    check_blackjack()
    check_bust()
    if player_val < 21:
        print(f"YOUR HAND IS WORTH {player_val}")

#executes commands
give_cards(user)
check_card_val(0, user)
check_card_val(1, user)
check_hand_val()
