# Make a list called sandwich_orders and fill it with the names of various
# sandwhiches. Then make and empty list called finished_sandwiches. Loop through
# the list of sandwich orders and print a message for each order, such as
# I made your tuna sandwich. As each sandwich is made, move it to the list of
# finished sandwiches. After all the sandwiches have been made print a message
# listing each sandwich that was made,

# Start with sandwiches that need to be made,
# and an empty list to hold made sandwiches.
sandwich_orders = ['the crazy dave', 'the big dave', 'the grateful dave']
finished_sandwiches = []

#welcome message
print("Welcome to Dave's Cosmic Subs!")

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
