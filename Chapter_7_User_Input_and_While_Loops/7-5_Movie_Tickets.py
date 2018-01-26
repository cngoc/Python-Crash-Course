# A movie theater charges different ticket prices depending on a person's age.
# If a person is under the age of 3, the ticket is free; if they are between
# 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

ticket = input("How many tickets are you buying today? ")
ticket = int(ticket)
total = 0
i = 0

if ticket == 1:
    age = input("How old are you? ")
    age = int(age)
    if age < 3:
        print("\nYour admission to the movies is free!")
    elif age < 12:
        print("\nYour movie ticket will cost $10.")
    else:
        print("\nYour movie ticket will cost $15.")

else:
    while True:
        try:
            below_3 = input("\nHow many person(s) are under the age of 3? ")
            below_3 = int(below_3)

        except below_3 > ticket:
            print ("\nThe number you enterered exceeded the number of tickets you intended to purchase.")
            continue

        else:
            total = below_3 * 0
            i += below_3

            if i == ticket:
                break


        #btwn_3_and_12 = input("How many person(s) are between the ages of 3 and 12? ")
        #btwn_3_and_12 = int(btwn_3_and_12)
        #total += btwn_3_and_12 * 10
        #i += btwn_3_and_12

        #if i >= ticket:
            break

        #over_12 = input("How many person(s) are over the age of 12? ")
        #over_12 = int(over_12)
        #total += over_12 * 15
        #i += over_12

        print("\nThe total price of all tickets will be: $" + str(total))
