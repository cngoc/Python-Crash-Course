#prompt user for what word they would like to see the count of in a text
print ("Note: Counting is case insensitive")
word_to_count = input("What word would you like me to count in \"Ambition and Success\" by Orison Swett Marden? ")

#find out how many times a word or phrase appears in a string
try:
	with open('Ambition and Success by Orison Swett Marden.txt') as file_object:
		contents = file_object.read()
		print (word_to_count+" is in the text "+str(contents.lower().count(word_to_count))+" times!")
except OSError:
	print ("File is not available to be able to count the words.")