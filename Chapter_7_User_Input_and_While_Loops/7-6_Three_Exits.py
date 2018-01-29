# Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statment to exit the loop when the user enters a 'quit' value.



prompt = "\nEnter a topping you would like: "
quit_prompt = prompt + "\n(Enter 'quit' when you are finished.) "
i = 0
active = True

topping_amount_known = input("Do you know how many toppings you'd like on your pizza? (y/n) ")
if topping_amount_known == 'y':
    topping_amount = input("How many toppings would you like in your pizza? ")
    topping_amount = int(topping_amount)

    while i < topping_amount:
        topping = input(prompt)
        print("\n" + topping + " has been added to your pizza.")
        i += 1

else:
    while active:
        topping = input(quit_prompt)

        if topping == 'quit':
            break
        else:
            print("\n" + topping + " has been added to your pizza.")

print("\nWe will now begin making your pizza with the toppings you specified!")
