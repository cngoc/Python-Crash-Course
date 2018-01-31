# Write a function called make_shirt() that accepts a size and the text of a
# message that should be printed on the shirt. The functin should print a
# sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.

def make_shirt(size, text):
    print("\nOn your size " + size + " shirt, the following message will be printed:")
    print(text)

make_shirt('small', 'positional argument')
make_shirt(text = 'keyword argument', size = 'small')
