#Read the files cat.txt and dog.txt
#Print the contents of the file to the screen.
#Wrap code in a try-except block to catch the FileNotFound error, and fail silently if a file is missing.

try:
	with open('cats.txt') as file_object:
		contents = file_object.read()
		print(contents)
except OSError:
	pass
	
try:
	with open('dogs.txt') as file_object:
		contents = file_object.read()
		print(contents)
except OSError:
	pass
