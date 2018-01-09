print("All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("\nMy favourite foods are:")
#print(my_foods)
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
#print(friend_foods)
for food in friend_foods:
    print(food)
