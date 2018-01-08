#exercise directions
print("Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal. \nModify your program to print a statement about each animal, such as A dog would make a great pet. \nAdd a line at the end of your program stating what these animals have in common. You could print a sentence such as any of these animals would make a great pet! \n")

#creating the list of animals
animals = ['jellyfish', 'mantis shrimp', 'sea cucumber', 'sea slugs']

#printing just the animal names
for animal in animals:
    print(animal.title())

print('\n')

#printing the animal names with a sentence that iterates.
for animal in animals:
    print(animal.title() + " are very unique.")

#printing sentence to summarize what they have in common
print("\nAll of these unique creatures can be found in the ocean!")
