# Make a list of magician's names. Pass the list to a function called
# show_magicians(), which prints the name of each magician in the list.

magicians = ['justin willman', 'martin brock', 'chipper lowell']

def show_magicians():
    """Return the names of the magicians"""
    for magician in magicians:
        print (magician.title())

show_magicians()
