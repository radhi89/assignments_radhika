"""Write a program to generate and print another tuple whose 
values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)."""
seq = (1,2,3,4,5,6,7,8,9,10)
even_tuple = filter(lambda x: x % 2 == 0,seq ) 
print("Even numbers in tuple :",tuple(even_tuple))
		