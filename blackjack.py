############### Blackjack Project #####################

import random


def get_card(cards):
    card = random.choice(deck)
    cards.append(card)
    for c in cards:
        if c == 11 and sum(cards) > 21:
            index = cards.index(c)
            cards[index] = 1
    return cards


def is_blackjack(seq):
    if sum(seq) == 21:
        return True
    else:
        return False


def new_game():

    for _ in range(2):
        get_card(user_cards)
        get_card(dealer_cards)
    print(user_cards)
    print(dealer_cards[0],"X")
    print(dealer_cards)


def is_game_over(user, dealer):
    if sum(dealer) == 21 and sum(user) != 21:
        winner = "Dealer"
        return True, winner

    elif sum(user) == 21 and sum(dealer) != 21:
        winner = "Player"
        return True, winner
    elif sum(dealer) > 21:
        winner = "Player"
        return True, winner
    elif sum(user) > 21:
        winner = "Dealer"
        return True, winner
    elif sum(dealer) > sum(user):
        winner = "Dealer"
        return True, winner
    elif sum(user) > sum(dealer):
        winner = "Player"
        return True, winner
    else:
        winner = "Draw"
        return False, winner


def dealer_turn(dealer):
    while sum(dealer) < 17:
        get_card(dealer)
    return dealer

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []
hit = ""

# ascii art source https://www.asciiart.eu/miscellaneous/playing-cards
print("""          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
Blackjack|  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
""")

new_game()
#user_cards = [11,3]
if is_blackjack(user_cards):
    print("we got 11")
    print("User has blackjack")
if is_blackjack(dealer_cards):
    print("Dealer has blackjack")

while hit != "n" and sum(user_cards) <= 21:
    hit = input("Do you want a new card? 'y' to hit or 'n' to stand:\n")
    if hit == "y":
        user_cards = (get_card(user_cards))
        print(user_cards)

dealer_turn(dealer_cards)
result = is_game_over(user_cards, dealer_cards)
if result[0]:
    print(f"Game over, winner is {result[1]}")
print(user_cards)
print(sum(user_cards))
print(dealer_cards)
print(sum(dealer_cards))

