print("Start with your program from Exercise 4-1 (Page 60). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following: \nAdd a new pizza to the original list. \nAdd a different pizza to the list friend_pizzas. \nProve that you have two separate lists. Print the mesage, My favorite pizzas are:, and then use a for loop to print the first list. Print the message, My friend\'s  favorite pizzas are:/ and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.")

pizzas = ['kosmic karma', 'pacific rim', 'funky q. chicken', 'holy shiitake pie']

for pizza in pizzas:
        print(pizza.title() + " is one of my favorite pizzas from Mellow Mushroom!")

print("\nPizza overall, is one of my favorite foods!")


#the initial copy of pizzas to friend_pizzas
friend_pizzas = list(pizzas[:])

#using append function to add a new pizza to the original list pizzas
pizzas.append('house special')

#using append function to add a new pizza to the list friend_pizzas
friend_pizzas.append('mighty meaty')

#printing list pizzas
print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

#print list friend_pizzas
print("\nMy friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
