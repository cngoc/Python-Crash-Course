# Start with your class from Exercise 9-1. Create three different instances
# from the class, and call describe_restaurant() for each instance.

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
general_muir = Restaurant('the general muir', 'delicatessen')
le_fat = Restaurant('le fat', 'vietnamese')
rise_n_dine = Restaurant('rise-n-dine', 'american')

general_muir.describe_restaurant()
le_fat.describe_restaurant()
rise_n_dine.describe_restaurant()


