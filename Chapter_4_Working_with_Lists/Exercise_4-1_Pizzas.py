#Exercise 4-1 instructions
print("Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza. \nModify your for loop to print a sentence using the name of the pizza instead of printing just the name of pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza. \nAdd a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza! \n")

#creating the list
pizzas = ['kosmic karma', 'pacific rim', 'funky q. chicken', 'holy shiitake pie']

#going through the list to print out a statement that applies to each value in the list
for pizza in pizzas:
        print(pizza.title() + " is one of my favorite pizzas from Mellow Mushroom!")

#a sentence to summarize my love for pizza.
print("\nPizza overall, is one of my favorite foods!")
