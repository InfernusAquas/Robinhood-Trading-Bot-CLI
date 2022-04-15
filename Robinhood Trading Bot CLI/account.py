class Account:
# Account takes a nested dictionary of my_stocks (the user's stocks)
    def __init__(self, dict_userStocks):
        self.getAccountInfo(dict_userStocks)


    def getAccountInfo(self, dict_userStocks):
        stockTickersOwned = list(dict_userStocks.keys())

        i = 0
        for x in stockTickersOwned:
            # break if we are out of bounds
            if(i>len(stockTickersOwned)): break
            try:
                print("\n{:.4} {}, w/ a PE Ratio of: {:.6}\nAvg. ${:.4} / curr. ${:.4}\n${}".format(
dict_userStocks[stockTickersOwned[i]]['quantity'],
dict_userStocks[stockTickersOwned[i]]['name'], 
dict_userStocks[stockTickersOwned[i]]['pe_ratio'],
dict_userStocks[stockTickersOwned[i]]['average_buy_price'],
dict_userStocks[stockTickersOwned[i]]['price'],
dict_userStocks[stockTickersOwned[i]]['equity_change']))
                i = 1 + i

            except: 
            # When pe_ratio is not available
                print("\n{:.4} {}, w/ a PE Ratio of: 0\nAvg. ${:.4} / curr. ${:.4}\n${}".format(
dict_userStocks[stockTickersOwned[i]]['quantity'],
dict_userStocks[stockTickersOwned[i]]['name'],
dict_userStocks[stockTickersOwned[i]]['average_buy_price'],
dict_userStocks[stockTickersOwned[i]]['price'],
dict_userStocks[stockTickersOwned[i]]['equity_change']))
            i = 1 + i