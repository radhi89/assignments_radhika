#Read and print number of lines, words and characters in the given file.


file_object1= open("sample.txt","w+")
file_object1.write("Hello world!\nNew Job\nNew Place\nExcited\nLove Python")
file_object1.close()


file_lines = 0
file_words = 0
file_char = 0

file_object = open("sample.txt","r")

print(file_object.read())
file_object.close()

file_object = open("sample.txt","r")
for line in file_object:
	words = line.split()

	file_lines+=1
	file_words+= len(words)
	file_char+= len(line)

print("No of lines in file : {}".format(file_lines))
print("No of words in file : {}".format(file_words))
print("No of characters in file : {}".format(file_char))