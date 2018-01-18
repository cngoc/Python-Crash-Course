# Start with the program you wrote for Exercise 6-1 (page 102). Make two new
# dictionaries representing different people, and store all three dictionaries
# in a list called people. Loop through your list of people. As you loop
# through the list, print everything you know about each person.

tsukimi = {
    'first_name': 'tsukimi',
    'last_name': 'kurashita',
    'age': '18',
    'city': 'tokyo'
    }

banba = {
    'first_name': 'banba',
    'last_name': 'unknown',
    'age': '8, due to being born in a leap year.',
    'city': 'tokyo'
    }

shu = {
    'first_name': 'shu',
    'last_name': 'koibuchi',
    'age': '30',
    'city': 'tokyo'
}

people = [tsukimi, banba, shu]

for person in people:
    print("\n" + str(person))
