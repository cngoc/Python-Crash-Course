# Write a function that accepts a list of items a person wants on a sandwhich.
# The function should have one parameter that collects as many items as the
# function call provides, and it should print a summary of the sandwhich that is
# being ordered. Call the function three times, using a different number of
# arguments each time.

def make_sandwiches(*toppings):
    """summarize the list of sandwich toppings requested."""
    print("\nI am making a sandwich with the following toppings: ")
    for topping in toppings:
        print(topping.title())

make_sandwiches('lettuce' , 'tomato', 'tuna')
make_sandwiches('onions', 'veggie patty')
make_sandwiches('cheese')
