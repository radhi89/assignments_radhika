"""Define a class named Circle which can be constructed by a
 radius. The Circle class has a method which can compute the area."""
from math import pi


class Circle():
	def __init__(self):
		self.radius = ""
		self.area = ""
	
	def Area(self,r):
		self.radius = r
		self.area = pi * (self.radius**2)
		print("Area of Circle with radius {} is : {}".format(self.radius,self.area))

r = int(input("Enter the radius:"))
circle1 = Circle()
circle1.Area(r)

	