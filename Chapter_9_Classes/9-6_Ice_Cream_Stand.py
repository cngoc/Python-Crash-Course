# An ice cream stand is a specific kind of restaurant. Write a class called
# IceCreamStand that inherits from the restaurant class you wrote in Exercise
# 9-1 or Exercise 9-4. Either version of the class will work: just pick the one
# you like better. Add an attribute called flavors that stores a list of ice
# cream flavors. Write a method that displays these flavors. Create an instance
# of IceCreamStand, and call this method.

class Restaurant():
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display information about the restaurant."""
        print(self.cuisine_type.capitalize() + " is the type of food that "
            + self.restaurant_name.title() + " is known for.")

"""Creating a child class from the parent Restaurant"""
class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to ice cream stands."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)

        """Initialize attributes specific to an ice cream stand."""
        self.flavors = ['queen city cayenne',
        'middle west whiskey and pecans',
        'coffee with cream and sugar']

    def display_flavors(self):
        print("\n" + self.restaurant_name.title() + " has the following ice cream flavors:")
        for flavor in self.flavors:
            print(flavor.title())

jenis = IceCreamStand('jenis', 'gourmet ice cream')
jenis.describe_restaurant()
jenis.display_flavors()
