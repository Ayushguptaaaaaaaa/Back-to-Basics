logo = r'''
                         ___________
                        '._==_==_=_.'
                        .-\:      /-.
                       | (|:.     |) |
                        '-|:.     |-'
                          \::.    /
                           '::. .'
                             ) (
                           _.' '._
                          `"""""""`
      ____  _ _           _      _             _   _
     | __ )| (_)_ __   __| |    / \  _   _  __| |_(_) ___  _ __
     |  _ \| | | '_ \ / _` |   / _ \| | | |/ __| __| |/ _ \| '_ \
     | |_) | | | | | | (_| |  / ___ \ |_| | (__| |_| | (_) | | | |
     |____/|_|_|_| |_|\__,_| /_/   \_\__,_|\___|\__|_|\___/|_| |_|

              *** WELCOME TO THE BLIND AUCTION ***
'''
print(logo)

restart="yes"

count=0
highest={}

while(restart=='yes'):
    name=input("What is your name: ")
    bid=int(input("Bidding amount: $" ))
    if count<bid:
        count=bid
        highest[name]=count
    restart=input("Do you have any other players? 'Yes' or 'No': ").lower()
    print("\n"*100)



# Method 1: using max()
# print(f"The Bid is won by {max(highest, key=highest.get)} with a bid of ${max(highest.values())}")

# Method 2: using a loop
winner = ""
winning_bid = 0
for bidder in highest:
    if highest[bidder] > winning_bid:
        winning_bid = highest[bidder]
        winner = bidder

print(f"The Bid is won by {winner} with a bid of ${winning_bid}")
    
