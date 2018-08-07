#Write a program that prompts for the user's favorite number. Use json.dump() to store this number in a file.
#Write a separate program that reads in this value and prints the message, "I know your favorite number! It's ...!"
import json

favNum = input("What is your favorite number? ")
filename = 'favNum.json'
with open(filename, 'w') as f_obj:
	json.dump(favNum, f_obj)
