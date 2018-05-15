#Open a blank file in your text editor and write a frew lines summarizing
#what you've learned about in Python so far. Start each line with the phrase
#In Python you can... Save the file as learning_python.txt in the same
#directory as your exercises from this chapter. Write a program that reads the
#file and prints what you wrote three times. Print the contents once by reading
#in the entire file, once by looping over the file object, and once by storing
#the lines in a list and then working with them outside the with block.

#reading the file learning_python.txt and printing contents
with open ('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

#looping over the file object
#.rstrip removes the newline each time it is printed
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

#storing the lines in a list
print("")
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
#and then working with them outside the with box
for line in lines:
    print(line.rstrip())
