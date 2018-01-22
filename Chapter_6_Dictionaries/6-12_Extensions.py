# We're now working with examples that are complex enough that they can be
# extended in any number of ways. Use one of the example programs from this
# chapter, and extend it by adding new keys and values, changing the context
# of the program or improving the formatting.
# pizza.py

#needed to be able to do regular expressions
import re
# function provided by Python documentation on how to address .title() mishandle
# of immediate letter after apostophe being captialized.
def titlecase(s):
     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
        lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(),s)

#store information about a pizza being ordered.
pizzas = {
    'socrate\'s revenge': {
    'crust': 'regular',
    'sauce': 'olive oil',
    'toppings': ['minced garlic', 'mozzarella', 'fontina', 'spinach', 'black olives', 'feta', 'red onions', 'tomatoes'],
    },

    'porky fig': {
    'crust': 'regular',
    'sauce': 'fig jam',
    'toppings': ['mozzarella', 'prosciutto', 'carmalized red onions', 'gorgonzola'],
    }
}
# summarize the order.
for pizza, pizza_info in pizzas.items():
    print("\nYou ordered the " + titlecase(pizza))

    # assigning the value that is a list to a variable
    crust = pizza_info['crust']
    sauce = pizza_info['sauce']
    toppings = pizza_info['toppings']

    print("Crust: " + crust.title())
    print("Sauce: " + sauce.title())

    print("Toppings:")
    for topping in toppings:
        print("\t" + topping.title())
