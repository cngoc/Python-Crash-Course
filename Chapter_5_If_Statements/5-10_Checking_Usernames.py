#Do the following to create a program that simulates how websites ensure that
#everyone has a unique username.
#Make a list of five or more usernames called current_users.
#Loop through the new_users list to see if each new username has already been
#used. If it has, print a message that the person will need to enter a new
#username. If a username has not been used, print a message saying that the
#username is available.
#Make sure your comparison is case insensitive. If 'John' has been used,
#'JOHN' should not be accepted.

current_users = ['administrator', 'Administrator', 'user1', 'admin', 'alex']
#current_users = []
new_users = ['admin', 'administrator', 'adver', 'advert', 'advertising']
#new_users = []

if new_users:
    for new_user in new_users:
        if new_user in current_users:
            print("Please enter a new username. " + new_user + " already exists.")
        else:
            print(new_user + " is available.")
else:
    print("There were no usernames to compare to the current database.")
