print("A buffet-style restaurant offer only five basic foods. Think of five simple foods, and store them in a tuple. \nUse a for loop to print each food the restaurant offers. \nTry to modify one of the items, and make sure that Python rejects the change. \nThe restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.")

foods = ('eggplant bharta', 'paneer kadhai', 'navratan shahi korma', 'shahi dal tadka', 'dal makhni')

#foods.append('hakka noodles')
#foods.append('gobi manchurian')

foods = ('hakka noodles', 'gobi manchurian', 'navratan shahi korma', 'shahi dal tadka')

print("\nUpdated menu!")
for food in foods:
    print(food)
