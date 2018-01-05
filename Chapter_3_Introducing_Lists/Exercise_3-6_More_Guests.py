#directions of the exercise
print("You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner. \nStart with you program from Exercise 3-4 or Exercise 3-5. Add a print statment to the end of your program. \nUse insert() to add one new guest to the beginning of your list. \nUse insert() to add one new guest to the middle of your list. \nUse append() to add one new guest to the end of your list. \nPrint a new set of invitation messages, one for each person in your list.")

#initial variable set to strings
invitations = ['Clifford the Big Red Dog', 'Franklin the Turtle', 'Arthur the Bear']
invite = ", you have been invited to my dinner!"
not_attending = ", is unable to make it to the dinner :("
updated_invite = ", I changed the guest list would you still like to attend the dinner?"


#initial set of invitations being delievered
print()
print(invitations[0] + invite)
print(invitations[1] + invite)
print(invitations[2] + invite)
print()

#Finding out our last guest is unable to make it
print(invitations[-1] + not_attending)

#inviting somone new to replace the guest that is unable to make it
invitations[-1] = 'Pee Wee'

#new round of invitations being sent
print()
print(invitations[-1] + invite)

#a bigger table is available
updated_invite = ", I was able to get a bigger table! I have invited more guests, would you still like to attend the dinner?"
#variable to find the middle of the array
middle_array = int(len(invitations)/2)
invitations.insert(0, 'Air Bud')
invitations.insert(middle_array, 'Sally')
invitations.append('Arnold')


#new invitations being sent b/c bigger table, those that have already confirmed.
print()
print(invitations[1] + updated_invite)
print(invitations[3] + updated_invite)
print(invitations[4] + updated_invite)

#invitations being sent to the added guests
print()
print(invitations[0] + invite)
print(invitations[middle_array] + invite)
print(invitations[-1] + invite)
print()
