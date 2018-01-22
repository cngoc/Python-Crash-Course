# Make a dictionary called cities. Use the names of three cities as keys in
# your dictionary of information about each city and include the country
# that the city is in, its approximate population, & one fact about that city.
# The keys for each city's dictionary should be something like country,
# population, and face. Print the name of each city and all of the information
# you have stored about it.

#nesting dictionaries.
cities = {
    'osaka': {
        'country': 'japan',
        'population': '2.691 million',
        'fact': 'Is known for hospitality!',
    },

    'chengdu': {
        'country': 'china',
        'population': '14.43 million',
        'fact': 'Chengdu locals speak a different dialect of Mandarian.',
    },

    'colombo': {
        'country': 'sri lanka',
        'population': '752,993',
        'fact': """When buddha visited Sri Lanka, It is believed his footprint
          was left atop Adam\'s Peak.""",
    },
    }

# for loop to go through each key and item
for city, city_info in cities.items():
    print("\nCity: " + city.title())

# assigning keys within the nested dictionary to a variable, to be able to use it.
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print("It is located in " + country.title() +
          " with a population of " + population + ".")
    print("Fun fact: " + fact)
