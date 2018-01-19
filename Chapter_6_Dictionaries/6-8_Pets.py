# Make several dictionaries, where the name of each dictionary is the name of a
# pet. In each dictionary, include the kind of animal and the owner's name.
# Store these dictionaries in a list called pets. Next, loop thorugh your list
# and as you do print everything you know about each pet.

opal = {
    'name': 'opal',
    'animal': 'elephant',
    'owner': 'up for adoption by the Colchester Zoo.'
    }

nzuri = {
    'name': 'nzuri',
    'animal': 'giraffe',
    'owner': 'up for adoption by the Colchester Zoo.'
    }

srey = {
    'name': 'srey ya',
    'animal': 'sun bear',
    'owner': 'up for adoption by the Colchester Zoo.'
    }

luco = {
    'name': 'luco',
    'animal': 'penguin',
    'owner': 'up for adoption by the Colchester Zoo.'
    }

heimdall = {
    'name': 'heimdall',
    'animal': 'meerkat',
    'owner': 'up for adoption by the Colchester Zoo.'
}

pets = [opal, nzuri, srey, luco, heimdall]

for pet in pets:
    print("\n"+ str(pet))
