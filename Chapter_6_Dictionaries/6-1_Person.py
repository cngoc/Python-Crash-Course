# Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which
# they live. You should have keys such as first_name, last_name,
# age, and city. Print each piece of information stored in your dictionary.

person = {'first_name': 'tsukimi', 'last_name': 'kurashita', 'age': '18', 'city': 'tokyo'}

print("The main character of Princess Jellyfish (Kuragehime) is " + person['first_name'].title() + " " + person['last_name'].title() +".")
print("She is " + str(person['age']) + " and lives in " + person['city'].title() + ".")
