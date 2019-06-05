#program to display a dictionary which shows {i,i*i}

n = int(input("Enter the integer : "))

d = {}
for x in range(1,n+1):
	d[x]= x**2

print(d)

	