"""Write a program that accepts a comma separated sequence of
words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
"""
values = input("Enter the words:")
li = values.split(',')
li.sort()
print("Sorted words are :",(',').join(li))