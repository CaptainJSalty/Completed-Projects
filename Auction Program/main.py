import os 

bids = {}
bid_continue = True

def find_highest_bidder (bidding_record): 
  highest_bid = 0 
  winner = ""

  for bidder in bidding_record:                                         #Looping through dictionary
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder 

  print(f"The winner is {winner} with a bid of ${highest_bid}")

while bid_continue == True:
  print("Welcome to the secret auction program.")
  name = input("What is your name?: ")
  price = int(input("What is your bid: $"))
  #Add name and price into a dictionary as the key and value 
  bids[name] = price #key is going to be the name and price is going to be the value                        Adding it to dictionary
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'")

  if should_continue == "yes": 
    os.system('cls')
  else: 
    os.system('cls')
    print("Welcome to the secret auction program.")
    find_highest_bidder(bids)
    bid_continue = False