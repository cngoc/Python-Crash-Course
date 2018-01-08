print("Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.\n")

numbers = list(range(1, 1000001))

print("The start of your list is " + str(min(numbers)) + "\nThe end of your list is " + str(max(numbers)) + "\nThe sum of your numbers in the list is " + str(sum(numbers)))
