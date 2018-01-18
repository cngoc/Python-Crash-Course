# Now that you know how to loop through a dictionary,
# clean up the code from Exercise 6-3 (page 102) by replacing your
# series of print statements with a loop that runs through the dictionary's
# keys and values. When you're sure that your loop works, add five more
# Python terms to your glossary. When you run your program again,
# these new words and meanings should automatically be included in the output.

defined_words = {
    'slice': """An object usually containing a portion of a sequence. A slice is
    created using the subscript notation, [] with colons between numbers when
    several are given, such as in variable_name[1:3:5]. The bracket (subscript)
    notation uses slice objects internally.""",

    'if statement': """allows you to examine the current state of a program and
    respond appropiately to that state.""",
    'method': """a function that takes a class instance as its
    first parameter.""",

    'list': """a built-in Python sequence. Despite its name it is more akin to
    an array in other languages than to a linked list since access to
    elements are O(1).""",

    'dictionary': """an associative array, where arbitrary keys are mapped
    to values."""}

# print ("Variable: " + defined_words['variable'])
# print("\nIf statement: " + defined_words['if statement'])
# print("\nmethod: " + defined_words['method'])
# print("\nlist: " + defined_words['list'])
# print("\ndictionary: " + defined_words['dictionary'])

for key, value in defined_words.items():
    print("\n" + key.title() + ": " + value)

print("""\n We are going to add additional words to our dictionary and sort
them into alphabetical order.""")

defined_words['object'] = """any data with state (attributes or value) and
defined behavior (methods). Also the ultimate base class of any
new-style class."""

defined_words['argument'] = """a value passed to a function (or method) when
calling it."""

defined_words['comment'] = """start with the hash character, and extend to the
end of the physical line."""

defined_words['for loop'] = """traditionally used when you a have a block of
code you want to repeat a fixed number of times."""

defined_words['attribute'] = """a value associaated with an object which is
referenced by name using dotted expressions."""


for key, value in sorted(defined_words.items()):
        print("\n" + key.title() + ": " + value)
