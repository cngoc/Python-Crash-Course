#Directions
print("Think of at least five places in the world you\'d like to visit. \nStore the locations in a list. Make sure the list is not in alphabetical order. \nPrint your list in its original order. Don't worry about printing the list neatly, just print it as a raw Python list. \nUse sorted() to print your list in reverse alphabetical order without changing the order of the original list. \nShow that your list is still in its original order by printing it again. \nUse reverse() to change the order of your list. Print the list to show that its order has changed. \nUse reverse() to change the order of your list again. Print the list to show it\'s back to its original order. \nUse sort() to change your list so it\'s stored in alphabetical order. Print the list to show that its order has changed.")

#Store the locations in a list
locations = ['tokyo', 'australia', 'cambodia']

print()
#The original list
print(locations)

#Use the function sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(locations))

#Show that your list is still in its original order by printing it again.
print(locations)

#Use reverse() to change the order of your list.
locations.reverse()

#Print the list to show that its order has changed.
print(locations)

#Use reverse() to change the order of your list again.
#print(locations.reverse()) returns none. Is it safe to assume that methods are weird when trying to use them on arrays?
#print(locations[].reverse()) returns invalid syntax
locations.reverse()

#Print the list to show it\'s back to its original order
print(locations)

#Use sort() to change your list so it\'s stored in alphabetical order.
locations.sort()

#Print the list to show that its order has changed.
print(locations)
