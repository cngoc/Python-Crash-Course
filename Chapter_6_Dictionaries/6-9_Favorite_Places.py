# Make a dictionary called favorite_places. Think of three names to use as
# keys in the dictionary, and store one to three favorite places for each
# person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and
# print each person's name and their favorite places.

#needed to be able to do regular expressions
import re
# function provided by Python documentation on how to address .title() mishandle
# of immediate letter after apostophe being captialized.
def titlecase(s):
     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                   lambda mo: mo.group(0)[0].upper() +
                              mo.group(0)[1:].lower(),s)

favorite_places = {
    'puppycat': ['bee\'s home', 'beach','space'],
    'bee': ['bee\'s home', 'cathead planet', 'beach'],
    'deckard': ['donut planet','deckard\'s home',]
    }

print('Puppycat\'s favorite places:')
for fav_places in favorite_places['puppycat']:
    print(titlecase(fav_places))

print('\nBee\'s favorite places:')
for fav_places in favorite_places['bee']:
    print(titlecase(fav_places))

print('\nDeckard\'s favorite places:')
for fav_places in favorite_places['deckard']:
    print(titlecase(fav_places))
