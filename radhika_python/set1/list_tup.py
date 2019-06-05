#take n inputs and generate a list and tuple

num = input("Enter the comma seperated values : ")
l = num.split(',')
t = tuple(l)
print("List :",l)
print("Tuple : ",t)
