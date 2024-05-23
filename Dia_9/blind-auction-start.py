import os
from art import logo

def bid_winner(dict, name, bid):
  dict[name] = bid
  #print(dict)
  
print(logo)
stop = False
bid_dict = {}
highest_bid = 0
winner = ""

while not stop:
    name = input("what is you name: ")
    bid = input("What's your bid?: ")
    other_bidders = input("Are there any other bidders: Type 'yes' or 'no'").lower()

    if other_bidders == "no":
        stop = True
    
    os.system('cls' if os.name == 'nt' else 'clear')

    bid_winner(dict=bid_dict, name=name, bid=bid)

for k in bid_dict:
    if int(bid_dict[k]) >= highest_bid:
        highest_bid = int(bid_dict[k])
        winner = k

print(f"The winner is {k} whith a bid of ${highest_bid}.")

  




#os.system('cls' if os.name == 'nt' else 'clear')
