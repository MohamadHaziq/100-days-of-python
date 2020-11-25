import art
import os

print (art.logo)

bids = {}
bidding_finished = False

def clear(): 
      # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of RM{highest_bid}")
        

while bidding_finished == False:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: RM"))
    bids[name] = price
    should_continue = input("Any other bidders ? Type 'yes' or 'no': ")
    if should_continue == 'no':
        bidding_finished = True
    elif should_continue == 'yes':
        clear()

clear()
find_highest_bidder(bids)