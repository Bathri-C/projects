import sys


def auction_statement(bids):
    """finding the highest amount of the bidder"""
    winner = ''
    highest_price = 0
    for bidder in bids:
        amount = bids[bidder]
        if amount > highest_price:
            highest_price = amount
            winner = bidder
    print(f'{winner} won the bid for {highest_price}')


Auction = True
bids = {}
while Auction:

    name = input('enter the name : ')
    price = float(input('enter your bid ! : $'))

    bids[name] = price

    if (input("any other's to continue Type \"y\" to continue \"n\" to final bids : ")) == 'n':
        Auction = False
        auction_statement(bids)
        sys.exit('Blind-Auction is closed 😎')
