#Write a program that prompts for the user's favorite number. Use json.dump() to store this number in a file.
#Write a separate program that reads in this value and prints the message, "I know your favorite number! It's ...!"
import json

filename = 'favNum.json'

try:
	with open(filename) as f_obj:
		favNum = json.load(f_obj)
		print ("I know your favorite number! It's " +favNum+"!")
except OSError:
	print("I don't know your favorite number :(")