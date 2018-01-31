# Write a program that polls users about their dream vacation. Write a prompt
# similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.

responses = {}

# set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the users name and response.
    name = input("\nWhat is your name? ")
    response = input("If you could visit only one place in the world, where would you go? ")

    # Store the response in a dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("\nWould you like to let another person respond? (y/n) ")
    if repeat == 'n':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would visit " + response + ".")
