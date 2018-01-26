# Write a loop that prompts the user to enter a series of pizza toppings until
# they enter a 'quit' value. As they enter each topping, print a message saying
# you'll add that topping to their pizza.

prompt = "\nEnter a topping you would like: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("\n" + topping + " has been added to your pizza.")

print("\nWe will now begin making your pizza with the toppings you specified!")
