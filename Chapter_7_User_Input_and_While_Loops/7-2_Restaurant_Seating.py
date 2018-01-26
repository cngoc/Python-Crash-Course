# Write a program that asks the user how many people are in their dinner group.
# If the answer is more than eight, print a message saying they'll have to wait
# for a table. Otherwise, report that their table is ready.

num_persons = input("How many people are in your dinner group? ")
num_persons = int(num_persons)

if num_persons > 8 :
    print("Your dinner group of " + str(num_persons) + " will have to wait for a table.")

else:
    print("Your table is ready!")
