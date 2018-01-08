print("Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following: \nPrint the message, The first three items in the list are:. Then use a slice to print the first three item from that program\'s list. \nPrint the message, Three items from the middle of the list are:. Use a slice to print three items from the middle of the list. \nPrint the message, The last three items in the list are:. Use a slice to print the last three items in the list. \n")

pizzas = ['kosmic karma', 'pacific rim', 'funky q. chicken', 'holy shiitake pie', 'mighty meaty']

#for pizza in pizzas:
        #print(pizza.title() + " is one of my favorite pizzas from Mellow Mushroom!")

#print("\nPizza overall, is one of my favorite foods!")

#printing as a sentence each time it goes through the list.
for pizza in pizzas[:3]:
    print("The first three items in the list are: " + pizza.title())

print()
for pizza in pizzas[1:4]:
    print("The three middle items in the list are: " + pizza.title())

print()
for pizza in pizzas[-3:]:
    print("The last three items in the list are: " + pizza.title())

#printing a list per sentence.
print("The first three items in the list are: " + str(pizzas[:3]))
print("The three middle items in the list are: " + str(pizzas[1:4]))
print("The last three items in the list are: " + str(pizzas[-3:]))
