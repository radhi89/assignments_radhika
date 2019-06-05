#Create a class with functions to add, subtract, multiply and division. Also write unit test for each function

class Calculator:
	"""docstring fos Calculator"""

	def __init__(self):
		pass



	def Add(self,a,b):
		self.sum = a + b
		return self.sum
		
	def Subtract(self,a,b):
		self.difference = a - b
		return self.difference
		
	def Multiplication(self,a,b):
		self.product = a * b
		return self.product
		
	def Division(self,a,b):
		self.div = a/b
		return self.div

		

	def DisplayResult(self):
		print("Sum : {}".format(self.sum))
		print("Difference : {}".format(self.difference))
		print("Product  : {}".format(self.product))
		print("Division : {}".format(self.div))

calculation = Calculator()

calculation.Add(3,4)
calculation.Subtract(5,4)
calculation.Multiplication(2,2)
calculation.Division(2,3)
calculation.DisplayResult()