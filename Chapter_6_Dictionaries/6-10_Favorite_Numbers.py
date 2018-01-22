# Modify your program from Exercise 6-2 so each person can have more than
# one favorite number. Then print each person's name along with their
# favorite numbers.

favorite_numbers = {
    'james': ['7', '1', '19'],
    'mary': ['3', '17', '2'],
    'john': ['8', '6', '9'],
    'patricia': ['4', '3', '12'],
    'michael': ['5', '13', '21']}

print("James has several favorite numbers: ")
for fav_num in favorite_numbers['james']:
    print(fav_num)

print("\nMary has several favorite numbers: ")
for fav_num in favorite_numbers['mary']:
    print(fav_num)

print("\nJohn has several favorite numbers: ")
for fav_num in favorite_numbers['john']:
    print(fav_num)

print("\nPatricia has several favorite numbers: ")
for fav_num in favorite_numbers['patricia']:
    print(fav_num)

print("\nMichael has several favorite numbers: ")
for fav_num in favorite_numbers['michael']:
    print(fav_num)
