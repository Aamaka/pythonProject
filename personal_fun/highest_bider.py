
from replit import clear

my_bid = {}
bidding_continue = False

while not bidding_continue:
    name = input("Enter your name: ")

    bid = input("Enter your bid price: ")

    my_bid[name] = bid

    users = input("Are there other bidders ? Enter 'yes' or 'no' ").lower()

    if users == "no":
        bidding_continue = True
    elif users == "yes":
        clear()
