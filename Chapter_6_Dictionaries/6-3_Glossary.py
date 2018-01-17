# A python dictionary can be used to model an actual dictionary. However, to
# avoid confusion, let's call it a glossary.
# Think of five programming words you've learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. Your might Print
# the word followed by a colon and then its meaning, or print the word on
# a second line. Use the newline character (\n) to insert a blank line between
# each word-meaning pair in your output.

defined_words = {
    'variable': 'a value that can change depending on the information passed to it.',
    'if statement': 'allows you to examine the current state of a program and respond appropiately to that state.',
    'method': 'a function that takes a class instance as its first parameter.',
    'list':'a data structure that is mutable (changable).',
    'dictionary': 'a collection of unordered values accessed by keys rather than by index.'}

print ("Variable: " + defined_words['variable'])
print("\nIf statement: " + defined_words['if statement'])
print("\nmethod: " + defined_words['method'])
print("\nlist: " + defined_words['list'])
print("\ndictionary: " + defined_words['dictionary'])
