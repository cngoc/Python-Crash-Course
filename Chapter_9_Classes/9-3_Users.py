
# Make a class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are typically
# stored in user profile. Make a method called describe_user() that prints
# a summary of the user's information. Make another method called greet_user()
# that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class User():
    """ A simple attempt to model users."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("\nFirst name: " + self.first_name.capitalize()
              + "\nLast name: " + self.last_name.capitalize())

    def greet_user(self):
        print("Welcome " + self.first_name.capitalize() + " " +
              self.last_name.capitalize())


"""Creating an instance of the class User"""
user_1 = User('sun', 'bak')
user_2 = User('wolfgang', 'bogdanow')
user_3 = User('kala', 'dandekar')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
