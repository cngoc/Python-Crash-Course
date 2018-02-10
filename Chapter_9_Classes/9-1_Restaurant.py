# Make a class called Restaurant. The __init__() method for Restaurant
# should store two attributes: a restaurant_name and a cuisine_type. Make a
# method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Restaurant():
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display information about the restaurant."""
        print(self.cuisine_type.capitalize() + " is the type of cuisine that " +
              self.restaurant_name.title() + " has on their menu.")

    def open_restaurant(self):
        """Display if the restaurant is open."""
        print(self.restaurant_name.title() + " is open.")

"""Creating an instance of the class Restaurant"""
restaurant = Restaurant('the general muir', 'delicatessen')

restaurant.describe_restaurant()
restaurant.open_restaurant()

