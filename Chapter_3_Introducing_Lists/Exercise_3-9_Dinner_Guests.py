print("Working with one of the programs from Exercises 3-4 through 3-7, use len() to print a message indicating the number of people you are inviting to dinner.")

guests = ['jim', 'shaun', 'john', 'kristiana', 'courtney', 'andria']

print()
print("Hello Chan, you have 10 seats available to join you. You have sent " + str(len(guests)) + " invitations so far.")

#str(len(guests)) seems so strange to me. I originally tried guests.len(). When the error told me that it cound't print b/c it isn't a string, I was like ok I guess I'll try str(guests.len()). third times a charm.
