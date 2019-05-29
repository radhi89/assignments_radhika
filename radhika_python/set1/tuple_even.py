"""Write a program to generate and print another tuple whose 
values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)."""
t=[]
for x in range(1,11):
	if (x%2==0):
		t.append(x)
	else:
		continue
print("Even numbers in tuple :",tuple(t))
		