# An administrator is a special kind of user. Write a class called admin
# that inherits from the user class you wrote in Exercise 9-3 or Exercise 9-5.
# Add an attribute, privileges, that stores a list of strings like "can add post",
# "can delete post", "can ban user", and so on. Write a method called
# show_privileges() that lists the administrator's set of privileges.
# Create an instance of Admin, and call your method.

class User():
    """A simple attempt to model users."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("Welcome " + self.first_name.capitalize() + " " +
            self.last_name.capitalize() +"!")

class Admin(User):
    """Represent aspects of a user specific to Admin."""
    def __init__(self, first_name, last_name):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name)

        """Initialize attributes specific to Admin"""
        self.privileges = ['delete user(s)', 'edit others posts',
            'view private messages', 'reset passwords']

    def show_privileges(self):

            print("\n" + self.first_name.capitalize() + " " + self.last_name.capitalize()
            + " is an Admin. \nBeing an admin has the following abilities:")

            for privilege in self.privileges:
                print("~ " +privilege.capitalize())

user = User('hello', 'kitty')
admin = Admin('gudetama', 'sanrio')

user.describe_user()
admin.describe_user()
admin.show_privileges()
