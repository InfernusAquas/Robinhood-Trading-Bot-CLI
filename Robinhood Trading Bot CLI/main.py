import robin_stocks.robinhood as r
from account import Account
from coin import Coin

looping = True

# Log into the account
while(looping):
    try: 
        r.login(store_session=True)
        # Gets the holdings of the account as a dict
        my_stocks = r.build_holdings()
        if(type(my_stocks) is dict):
            break
    except: print("\nImproper login details provided\n")

# Get user input 
while(looping):
    i = input("\n\nWhat would you like to do:\n1. Account - View all stock holdings" +
  "\n2. Coin\n3. Logout\n\n").lower()
  
    if(i == "account"):
        acc = Account(my_stocks)
    elif(i == "coin"):
        rs = r  
        coin = Coin(rs)
    elif(i == "logout"):
        r.authentication.logout()
        print("logged out - Application exiting")
        exit()
        break

    else: 
        print("Please select another option")