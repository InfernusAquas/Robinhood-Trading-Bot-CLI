from datetime import date
from datetime import datetime
from os.path import exists

class Utilities:
    # Utilities are meant for methods that can be easily reused between different funcs

	def getDate(self):
		'''Returns current date in str format: September 16, 2022'''
		today = date.today()
		d = today.strftime("%B %d %Y")
		return d

	def getTime(self):
		'''Returns current time in str format: '''
		time = datetime.now()
		currTime = time.strftime('%H:%M:%S')
		print(currTime)

	def doesExist(self, path:str):
		'''param(str=file_path)
		Checks if the file exists. If true = skip. False = createCSV()'''
		file_exists = exists(path)
		return file_exists