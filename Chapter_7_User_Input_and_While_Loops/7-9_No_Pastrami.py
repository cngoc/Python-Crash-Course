# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich
# 'pastrami' appears in the list at least three times. Add code near the
# begininning of your program to print a message saying the deli has run out of
# pastrami, and then use a while loop to remove all occurrences of 'pastrami'
# from sandwich_orders. Make sure no pastrami sandwiches end
# up in finished_sandwiches.

# Start with sandwiches that need to be made,
# and an empty list to hold made sandwiches.
sandwich_orders = ['pastrami',
    'the crazy dave',
    'pastrami',
    'the big dave',
    'the grateful dave',
    'pastrami']
finished_sandwiches = []
pastrami_count = 0
#welcome message
print("\nWelcome to Dave's Cosmic Subs!")
print("Today we are out of pastrami.\n")

# Remove all pastrami sandwhiches
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    pastrami_count += 1

# Make each sandwich until there are no more sadnwhiches to be made.
# Move each sandwich to list of finished_sandwiches.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("Making the " + current_sandwich.title() + " sandwich!")
    finished_sandwiches.append(current_sandwich)

# Display all made sandwiches
print("\nThe following sandwiches have been made today:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

print("\nWe were unable to fulfill " + str(pastrami_count) + " orders of pastrami today.")
