# Add an attribute called login_attempts to your User class from Exercise 9-3
# (page 166). Write a method called increment_login_attempts() that increments
# the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call login_attempts to make sure it was
# incremented properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.

class User ():

    def __init__(self, first_name, last_name, login_attempts):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Login attempt(s): " + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login attempts(s): " + str(self.login_attempts))


"""Creating an instance of class User"""
user = User('sun', 'bak', 3)
# Initial login attempts
print("Login attempt(s): " + str(user.login_attempts))

user.increment_login_attempts()
user.reset_login_attempts()
