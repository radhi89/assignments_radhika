"""Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
"""

class String_upper():
	"""docstring for ClassName"""
	def __init__(self):
		self.string = ""

	def getString(self):
		self.string = input("Type the string:")
	
	def printString(self):
		print("String in uppercase:",self.string.upper())


s = String_upper()
s.getString()
s.printString()

