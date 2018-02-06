# Start with your work from Exercise 2-10. Call the function
# make_great() with a copy of the list of magicians' names. Because
# the original list will be unchanged, return the new list and store
# it in a seperate list. Call show_magicians() with each list to show
# that you have one list of the original names and one list with the great
# added to each magician's name.

magicians = ['justin willman', 'martin brock', 'chipper lowell']
# the way the book teaches you to copy a list
the_greats = magicians[:]

# Precheur suggests this approach to copying a list
# http://henry.precheur.org/python/copy_list
the_greats_precheur = list(magicians)

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
        the_greats[i] = "the great " + the_greats[i]
        the_greats_precheur[i] = "the great " + the_greats_precheur[i]
        i += 1

make_great()
"""Displaying copied original list that has been modified"""
print (the_greats)
print (the_greats_precheur)
