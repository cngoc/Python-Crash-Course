# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as One of my favorite books is
# Alice in Wonderland. Call the function, making sure to include a book title
# as an argument in the function call.

def favorite_book(title):

    print("\n" + title.title() + (", is a favorite book of yours."))

title = input("\nWhat is a favorite book of yours? ")
favorite_book(title)
