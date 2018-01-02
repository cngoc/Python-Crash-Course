# Standard Hello World print statement.
print ("Hello, welcome to the world of Python.")

# Standard assigning string to variable.
message = "Hello, welcome to the world of Python variables."
print(message)

# Standard changing value of variable.
change = "I begin simply without change. Initial set for change."
print(change)
change = "I simply changed. Final set for change."
print(change)

# Learning about title method. It capitalizes the first letter of each word.
name = "ada lovelace"
print(name.title())

# Learning about the upper method. It capitalizes all the letters in a word.
word = "excited"
print(word.upper())

# Learning about the lower method. It lowercases all the letters in a word.
# Can be particularly useful for storing data.
# Many times you won't want to trust the capitalization that your users provide
# so you'll convert strings to lowercase before storing them.
word = "GLOOM"
print(word.lower())

# Learning about concatenation
first_name = "monty"
last_name = "python"
full_name = first_name + " " + last_name

print(full_name)

# Let's get a little more fancy with what we'be learned so far.
print("Hello, "+full_name.title() + "!")

# Let's upgrade the previous by storing to a variable
message = "Hello, "+full_name.title()+"! You have been stored as a variable."
print(message)

# Let's add a tab.
print("\tTabbed")

# What about a newline?
print("\nGoodbye 2017, hello 2018!")

# Combining tabs and new lines.
print("\nI can't help but be \nNervous \nTap tap tap \tTABBED!")

# Stripping whitespace
# Python can look for extra whitespace on the right and left sides of a string.
# To ensure that no whitespace exists at the right end of a string, use the rstrip() method
favorite_language = " python do you smash? "
# temporarily strips the right whitespace.
favorite_language.rstrip()
print(favorite_language)
# remove right whitespace permanently by storing to a variable.
favorite_language = favorite_language.rstrip()
print(favorite_language)
# remove left whitespace permanently by storing to a variable.
favorite_language = favorite_language.lstrip()
# remove both right and left whitespace permanently by storing to a variable.
print(favorite_language.strip())

# end of chapter 2 material. Ppcoming is exercises for chapter 2 that will be in seperate files.
