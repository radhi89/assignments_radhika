#Get a list of numbers from users and print the smallest odd number.

numbers = input("Enter a list of numbers:")
number_list = numbers.split(',')
odd_list = []
for i in range(0,len(number_list)+1):
	if (i%2!=0):
		odd_list.append(i)
odd_list.sort()
print("Smallest odd number in list",odd_list[0])
		