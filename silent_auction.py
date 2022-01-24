from os import system, name
from time import sleep


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


option_continue = True
while option_continue:
    winner = ""
    winning_bid = 0
    auctions = {}
    name = input("Please introduce your name: ")
    bid = input("Please introduce your bid: ")
    auctions[name] = float(bid)
    option_continue = input("Is there another bidder? 'y' for yes 'n' for no: \n")
    if option_continue == "y":
        clear()
        option_continue = True
    else:
        # check for winner here
        option_continue = False
        for auction in auctions:
            if auctions[auction] > winning_bid:
                winning_bid = auctions[auction]
                winner = auction
                clear()
        print(f"The winner is {winner} with a bid of ${winning_bid}")
