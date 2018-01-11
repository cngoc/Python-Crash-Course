#You don't have to limit the number of tests you create to 10.
#If you want to try more comparisons, write more tests and add them to
#conditional_test.py. Have at least one True and on False result for each
#of the following:
#Tests for equality and inequality with strings
#Tests using the lower() function (typo in the book? because lower() is a method...)
#Numerical tests involving equality and inequality, greater than and less than,
#greater than or equal to, and less than or equal to.
#Tests using the and keyword and the or keyword
#Test whether an item is in a list
#Test whether an item is not in a list

number = '23'
print("Is number == \'23\'? I predict True.")
print(number == '23')

print("Is number == \'10\'? I predict False.")
print(number =='10')

print("Is number == \'2 3\'? I predict False.")
print(number == '2 3')

print("Is number == 23 + 0? I predict False.")
print(number == 23 + 0)

print("Is number == str(eval('23+0'))? I predict True.")
print(number == str(eval('23+0')))

word = 'hygge'
print("Is word == 'HYGGE'.lower()? I predict True. ")
print(word == 'HYGGE'.lower())

print("Is 23 == 2+3 ? I predict False.")
print(23 == 2+3)

print("Is 25 < 23 < 15 ? I predict False.")
print(25 < 23 < 15)

print("Is 15 < 23 == 23 ? I predict True.")
print(15 < 23 == 23)

print("Is 15 > 23 == 23 ? I predict False.")
print(15 > 23 == 23)

print("Is 23 == 23 and 23 < 30 ? I predict True.")
print(23 == 23 and 23 < 30)

print("Is 23 == 23 + 1 or 23 == 25 - 2 ?  I predict True.")
print (23 == 23 + 1 or 23 == 25 - 2)

animals = ['cat', 'dog', 'llama']
print("Is \'llama\' in animals ? I predict True.")
print('llama' in animals)

print("Is \'lettuce\' not in animals ? I predict True.")
print('lettuce' not in animals)
