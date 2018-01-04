#directions of the exercise
print("You just heard that one of your guests can\'t make the dinner, so you need to send out a new set of invitations. You\'ll have to think of someone else to invite. \nStart with your program from Exercise 3-4. Add a print statement at the end of your program stating the name of the guest who can't make it. \nModify your list, replacing the name of the guest who can\'t make it with the name of the new perosn you are inviting. \nPrint a second set invitation messages, one for each person who is still in your list.")

#initial variable set to strings
invitations = ['Clifford the Big Red Dog', 'Franklin the Turtle', 'Arthur the Bear']
invite = ", you have been invited to my dinner!"
not_attending = ", is unable to make it to the dinner :("
updated_invite = ", I changed the guest list would you still like to attend the dinner?"

#initial set of invitations being delievered
print('\n')
print(invitations[0] + invite)
print(invitations[1] + invite)
print(invitations[2] + invite)
print('\n')

#Finding out our last guest is unable to make it
print(invitations[-1] + not_attending)

#inviting somone new to replace the guest that is unable to make it
invitations[-1] = 'Pee Wee'

#new round of invitations being sent
print()
print(invitations[-1] + invite)
print(invitations[0] + updated_invite)
print(invitations[1] + updated_invite)
