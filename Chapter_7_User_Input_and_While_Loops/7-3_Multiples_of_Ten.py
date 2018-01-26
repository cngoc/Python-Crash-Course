# Ask the user for a number, and then report whether the number is a
# a multiple of 10 or not.

num = input("Type in a number: ")
num = int(num)

if num != 0 and num % 10 == 0:
    print(str(num) + " is a multiple of 10!")

else:
    print(str(num) + " is NOT a multiple of 10!")
