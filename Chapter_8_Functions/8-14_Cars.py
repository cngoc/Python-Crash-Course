# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments. Call the
# function with the required information and two other name-value pairs, such
# as a color or an optional feature. Your function should work for a call like
# this one:
# car = make_car('subaru', 'outback', color = 'blue', tow_package=True)
# Print the dictionary that's returned to make sure all the information
# was stored correctly.

def car_info(manufacturer, model_name, **info):
    """Build a dictionary containing everything we know about the car."""
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['name'] = model_name
    for key, value in info.items():
        profile[key] = value
    return profile

car_profile = car_info('tesla', 'roadster',
    color = 'red multi-coat',
    cost_founders = '250000',
    top_speed = 'over 250 mph')

print(car_profile)
