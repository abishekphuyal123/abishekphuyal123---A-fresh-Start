# This is a simple silent auction program using while loop and dictionaries. 

from replit import clear 
# importing clear from replit module. 

print("Welcome to Silent Auction:")

bids = {} #  Empty Dictionary
go = True 

def highest_bid(bidding_record): # A function that uses for loop to loop through the dictionary to find the highest bid. 
  highest_bid = 0 
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner}, with a bid of ${highest_bid}.") # Prints out the highest bid. 

while go: # While Loop
  name = input("Enter your name: ")
  bid = int(input("Enter your bid amount: $"))
  bids[name] = bid
  cont = input("Any other bids? 'yes' or 'no'.").lower()
  if cont == "no":
    go = False
  elif cont == "yes":
    clear()

highest_bid(bids) # Calling the function. 

