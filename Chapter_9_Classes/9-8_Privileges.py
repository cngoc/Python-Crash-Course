# Write a seperate Privileges class. The class should have one attribute,
# privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance of
# Admin and use your method to show its privileges.

class User():
    """A simple attempt to model users."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("Welcome " + self.first_name.capitalize() + " " +
            self.last_name.capitalize() + "!")

class Admin(User):
    """Represent aspects of a user specific to Admin."""
    def __init__(self, first_name, last_name):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name)

class Privileges(Admin):
    def __init__(self, first_name, last_name):
        self.privileges = ['delete user(s)', 'edit others posts',
                    'view private messages', 'reset passwords']
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name)

    def show_privileges(self):
        print("\n" + self.first_name.capitalize() + " " + self.last_name.capitalize()
            + " is an Admin. \nBeing an Admin has the following abilities: ")

        for privilege in self.privileges:
            print("~ " + privilege.capitalize())

user = User('hello', 'kitty')
admin = Admin('gudetama', 'sanrio')
privilege = Privileges('gudetama', 'sanrio')

user.describe_user()
admin.describe_user()
privilege.show_privileges()
