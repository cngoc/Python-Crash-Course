print("Give me two numbers, and I'll add them.")

first_num = input("\nFirst number: ")
second_num = input("Second number: ")
try:
	answer = int(first_num) + int(second_num)
except ValueError:
	print("I need numbers in integer form to be able to perform addition!")
else:
	print(answer)
