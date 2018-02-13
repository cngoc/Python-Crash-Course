# Start with your program from Exercise 9-1 (page 166). Add an attribute called
# number_served with a default value of 0. Create an instance called restaurant
# from this class. Print the number of customers the restaurant has served,
# and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.
# Add a method called increment_number_served() that lets you increment the
# number of customers who've been served. Call this method with any number you
# like that could represent how many customers were served in, say, a day of
# business.

class Restaurant():
    """A simple attempt to model a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display information about the restaurant."""
        print(self.cuisine_type.capitalize() + " is the type of cuisine that " +
              self.restaurant_name.title() + " has on their menu.")

        """Display initial number served"""
        print("Customers served: " + str(self.number_served))

    def open_restaurant(self):
        """Display if the restaurant is open."""
        print(self.restaurant_name.title() + " is open.")

    def set_number_served(self):
        """Set the number served and display it."""
        self.number_served = 5
        print("Customers served: " + str(self.number_served))

    def increment_number_served(self, inum_served):
        """Set the increment value"""
        self.number_served += inum_served
        print("Customers served: " + str(self.number_served))


restaurant = Restaurant('falafal king', 'mediterranian asian fusion')
restaurant.describe_restaurant()
restaurant.set_number_served()
restaurant.increment_number_served(23)

