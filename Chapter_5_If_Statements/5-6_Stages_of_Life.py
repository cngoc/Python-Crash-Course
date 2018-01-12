#Write an if-elif-else chain that determines a person's stage of life.
#Set a value for the variable age, and then:
#If the person is less than 2 years old, print a message that the person
#is a baby.
#If the person is at least 2 years old but less than 4, print a message that
#the person is a toddler.
#If the person is at least 4 years old but less than 13, print a message that
#the  person is a kid.
#if the person is at least 13 years old but less than 20, print a message that
#the person
#If the person is at least 20 years old but less than 65, print a message
#that the person is an adult.
#If the person is age 65 or older, print a message that the person is an elder.

import random

age = random.randrange(123)

if age < 2:
    print(str(age) + ", what a cute baby!")

elif age < 4:
    print(str(age) +  ", getting evil toddler, and you don't even know it!")

elif age < 13:
    print(str(age) + ", getting some sense into ya, kid.")

elif age < 20:
    print(", oh teenage angst.")

elif age < 65:
    print(str(age) + ", welcome to adulthood! Responsibilities are real.")
    
else:
    print(str(age) + ", yes, yes. Oh wise elder!")
