#Read the files cat.txt and dog.txt
#Print the contents of the file to the screen.
#Wrap code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing.

try:
	print("Cat roll call:")
	with open('cats.txt') as file_object:
		contents = file_object.read()
		print(contents)
except OSError:
	print("cats.txt file not found!\n")
	
try:
	print("Dog roll call:")
	with open('dogs.txt') as file_object:
		contents = file_object.read()
		print(contents)
except OSError:
	print("dogs.txt file not found!")
