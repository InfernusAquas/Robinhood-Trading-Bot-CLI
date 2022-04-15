import csv
import json
import random
from utilities import Utilities
from collections import defaultdict

class Coin:
	# Coin will randomly generate two stocks and flip a coin 101 times
	# each stock will be assigned a head/tail. Whichever stock earns 
	# the most flips. The algo will buy $xl of that stock
	def __init__(self, robin_stocks):
		# assign local vars/objs
		self.dir = 'C:/Users/Joshua/source/repos/Robinhood Trading Bot CLI/Robinhood Trading Bot CLI/stocks.csv'
		self.utilities = Utilities()

		# check if stocks.csv exists. If not make file
		if(self.utilities.doesExist(self.dir) == False):
			self.createStocksCSV()

		# assigns random stocks
		self.buyTicker(robin_stocks, self.fiftyFifty((self.assRanStocks(self.loadStocks()))))

	def loadStocks(self):
		'''Returns contents of data.json as a dict'''
		# Opens the JSON file
		f = open('data.json')
	
		# Returns JSON object as a dictionary
		data = json.load(f)

		# Stores the data obj as a list
		x = data.get('tickers')  

		# Stores the passed list as a dictionary
		dct = self.listToDict(x)

		# Close the file 
		f.close()
		return dct

	def listToDict(self, ls:list):
		'''params(list)
		Returns a dictionary given a passed list'''
		res = defaultdict(list)
		for sub in ls:
			for key in sub:
				res[key].append(sub[key])
		return dict(res)
  
	def assRanStocks(self, dct:dict):
		'''param(dict)
		Returns a dictionary of two random stocks with values of 0'''
		try: ticker1 = dct['ticker'][random.randint(0, len(dct['ticker']))]
		except: ticker1 = dct['ticker'][-1]
	  
		try: 
			ticker2 = dct['ticker'][random.randint(0, len(dct['ticker']))]
			while(ticker2 == ticker1):
				ticker2 = dct['ticker'][random.randint(0, len(dct['ticker']))]
		except: 
			ticker2 = dct['ticker'][-1]
			while(ticker2 == ticker1): 
				ticker2 = dct['ticker'][random.randint(0, len(dct['ticker']))]

		tickerRecords = {ticker1: 0, ticker2: 0}
		return tickerRecords

	def fiftyFifty(self, tickerRecords:dict):
		'''param(dict)
		Generates 0,1 randomly 101 times, returning a str'''
		# Generates 0,1 randomly 101 times, returning the stock it lands on most
		for x in range(0, 101):
			x = random.randint(0,1)
			keys = list(tickerRecords.keys())
			ticker1 = keys[0]
			ticker2 = keys[1]

			if(x == 0):
				tickerRecords[ticker1] += 1
			else:
				tickerRecords[ticker2] += 1

		values = list(tickerRecords.values())
		values.sort()
		ticker = list(tickerRecords.keys())[list(tickerRecords.values()).index(values[-1])]
		return ticker

	def buyTicker(self, robin_stocks, ticker:str):
		'''Param(robin_stocks api, str=ticker)
		Purchases $5 of the passed str'''
		#robin_stocks.orders.order_buy_fractional_by_price(ticker:str, 5)
		print("\nCongratulations, you have just purchased $5 of {}".format(ticker))

	def createStocksCSV(self):
		'''param(path:str)
		Creates stocks.csv in the working dir'''
		# The 'w' option deletes any prev. file and creates a new file
		# s = stocks.csv
		with open('stocks.csv', mode='w') as s:
			stockwriter = csv.writer(s, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			stockwriter.writerow(['Ticker', '$ Amount Bought', 'Date', 'Time', 'Avg. Cost'])

	def updateCSV(self, ticker:str, qty_bought:float, date, time, avg_cost:float):
		print("update soon")