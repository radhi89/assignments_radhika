"""
Let 'a' be the list of users who likes a post! I want to get displayed as below.
eg 1 :-       a = []
Output :      Nobody likes This
eg 2 :-       a = ['Alice']
Output :      Alice likes This
eg 3 :-       a = ['Alice','Bob']
Output :      Alice and Bob likes This
eg 4 :-       a = ['Alice', 'Bob', 'Charls']
Output :      Alice, Bob and Charls likes This
eg 5 :-       a = ['Alice', 'Bob', 'Charls','Denny']
Output :      Alice, Bob and 2 others likes This
eg 6 :-       a = ['Alice', 'Bob', 'Charls','Denny','Emely']
Output :      Alice, Bob and 3 others likes This
"""



names =[names for names in input("Enter the names of people who likes the post:").split(',')]
print(names)
n = len(names)
if (names==['']):
	print("nobody likes this")
elif(n==1):
	print("{} likes this".format(names[0]))
elif(n==2):
	print("{} and {} likes this".format(names[0],names[1]))
elif(n==3):
	print("{}, {} and {} likes this".format(names[0],names[1],names[2]))
else:
	print("{},{} and {} likes this".format(names[0],names[1],n-2))

	
