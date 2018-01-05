#directions of the exercise
print("You just found out that your new dinner table won\'t arrive in time for the dinner, and you have space for only two guests. \nStart with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner. \n Use pop() to remove guests from your lisdt one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.")

#initial variable set to strings
guests = ['Clifford the Big Red Dog', 'Franklin the Turtle', 'Arthur the Bear']
invite = ", you have been invited to my dinner!"
not_attending = ", is unable to make it to the dinner :("
updated_invite = ", I changed the guest list would you still like to attend the dinner?"


#initial set of guests being delievered
print()
print(guests[0] + invite)
print(guests[1] + invite)
print(guests[2] + invite)
print()

#Finding out our last guest is unable to make it
print(guests[-1] + not_attending)

#inviting somone new to replace the guest that is unable to make it
guests[-1] = 'Pee Wee'

#new round of guests being sent
print()
print(guests[-1] + invite)

#a bigger table is available
updated_invite = ", I was able to get a bigger table! I have invited more guests, would you still like to attend the dinner?"
#variable to find the middle of the array
middle_array = int(len(guests)/2)
guests.insert(0, 'Air Bud')
guests.insert(middle_array, 'Sally')
guests.append('Arnold')


#new invitations being sent b/c bigger table, those that have already confirmed.
print()
print(guests[1] + updated_invite)
print(guests[3] + updated_invite)
print(guests[4] + updated_invite)

#guests being sent to the added guests
print()
print(guests[0] + invite)
print(guests[middle_array] + invite)
print(guests[-1] + invite)
print()

#Can't invite them all notification
print("Sorry Chan! Turns out there was a problem with our reservation system. You can only have two guests with you. Again, we apologize for the inconvenience.")
print()

#new notification b/c table has shrunk
rejected = ", I\'m sorry the restaurant has notified me that I can only have two guests at the table with me. Please know your friendship is important to me. Thank you for being awesome and understanding!"

#Using pop() to remove guests from the list
print()
print(guests.pop(5) + rejected)
print(guests.pop(4) + rejected)
print(guests.pop(3) + rejected)
print(guests.pop(2) + rejected)


#sending invite to left over two in array
updated_invite = ", you are still invited to my dinner. There will only be three of us instead of seven. The restaurant notified me that their system made a mistake and ended up giving us a smaller table. I look forward to dining with you!"

print()
#to confirm that array only left with two
#print(guests)

print(guests[0] + updated_invite)
print(guests[1] + updated_invite)
print()



#clearing the array using del()
del guests[-1]
del guests[-1]
print(guests)
