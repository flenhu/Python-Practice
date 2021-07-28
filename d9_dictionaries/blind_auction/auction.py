from replit import clear


from art import logo

print(logo)

def highest(bid_record):
  highest_bid = 0
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if highest_bid < bid_amount:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
finished = False

while not finished:
  name =input("What's your name?: ")
  price = int(input("What is your bid? $"))
  bids[name] = price
  bid_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
  if bid_continue == "no":
    finished = True
    highest(bids)
  elif bid_continue == "yes":
    clear()


