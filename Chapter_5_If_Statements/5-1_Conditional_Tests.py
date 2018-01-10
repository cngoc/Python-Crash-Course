#Write a series of conditional tests.
#Print a statement describing each test and your prediction for the results of
#each test. Your code should look something like this.
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')

#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')

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

#If I were to number == eval('23+0') it would return false b/c it is
#comparing a string to an integer.
