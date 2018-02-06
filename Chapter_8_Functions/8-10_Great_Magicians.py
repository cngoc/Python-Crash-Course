# Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list
# of magicians by adding the phrase the Great to each magician's name.
# Call show_magicians() to see that the list has actually been modified.

magicians = ['justin willman', 'martin brock', 'chipper lowell']
i = 0

def show_magicians():
    """Return the names of the magicians"""
    for magician in magicians:
        print (magician.title())

show_magicians()

def make_great():
    """Modifying elements in the list to include the great in front of name"""
    #to address unboundLocalError we have global
    global i
    while i < 3:
        magicians[i] = "the great " + magicians[i]
        i += 1

make_great()
"""Displaying modified original list"""
print (magicians)
