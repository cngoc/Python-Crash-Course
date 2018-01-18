# Use the code in favorite_languages.py (page 104).
# Make a list of people who should take the favorite languages poll.
# Include some names that are in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already
# taken the poll, print a message thanking them for responding. If they have
# not yet taken the poll, print a message inviting them to take the poll.

potental_poll_persons = ['edna', 'edward', 'phil', 'chad']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

for name in potental_poll_persons:
    print("\n" + name.title())

    if name in favorite_languages.keys():
        print(" Thank you for taking the poll.")
        print(" I see your favorite language is "
        + favorite_languages[name].title() + ".")

    else:
        print(" Hello " + name.title() + ", what is your favorite language?")
