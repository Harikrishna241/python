# we need to find the highest bidder 
print("******************** welcome to bidding *****************")
def bidding_auction(auction_data):
    max=0;
    for bidder in auction_data.keys():
        bid_amount=auction_data[bidder]
        if(max<bid_amount):
            max=bid_amount
        else:
            max=max;
    print(f"the bidder {bidder} won the bid with highest amount {bid_amount}") 
    return None  
Auction_bidding_data={}
Is_bidding="True"
while (Is_bidding=="True"):     
    name=input("what is your name:")
    bid_amount=int(input("pleas tell me the amount :"))
    Auction_bidding_data[name]=bid_amount
    Is_anyone_there=input("Is any one ther 'yes' or 'no': ")
    if(Is_anyone_there=="yes"):
        print("please come the next person")    
    else:
        print("Now the bidding entering names is closed")
        bidding_auction(Auction_bidding_data)
        Is_bidding="False"
        
        
        
   
         