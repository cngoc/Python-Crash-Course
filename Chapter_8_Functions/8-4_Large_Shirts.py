# Modify the make_shirt() function so that shirts are large by default with
# a message that reads I love Python. Make a large shirt and a medium shirt
# with the default message, and a shirt of any size with a different message.

def make_shirt(text = 'I love Python.', size = 'large'):
    print("\nOn your size " + size + " shirt, the following message will be printed:")
    print(text)

make_shirt()

make_shirt(size = 'medium')

make_shirt(size = 'small', text = "Resist the default!")
