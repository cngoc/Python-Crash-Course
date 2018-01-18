# Make a dictionary containing three major rivers and the country each river
# runs through. One key-value pair might be 'nile' : 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

major_rivers ={
    'amazon': 'brazil',
    'blue nile': 'ethiopia',
    'yangtze': 'china',
    'danube': 'germany',
    'ganges': 'india' }

print("\nA list of major rivers:")
for key in major_rivers.keys():
    print(key.title())

print("\nA list of countries where a major river can be found:")
for value in major_rivers.values():
    print(value.title())

print("")
for key, value in sorted(major_rivers.items()):
    print(key.title() + " river flows through " + value.title() + ".")
