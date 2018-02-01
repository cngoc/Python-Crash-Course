# Write a function called city_country() that takes in the name of a city and
# its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city country pairs, and print the value
# that's returned.

def city_country(city, country):
    city_n_country = city.title() + ', ' + country.title()
    return(city_n_country)

print(city_country('atlanta', 'united states of america'))
print(city_country('san jose', 'costa rica'))
print(city_country('siem reap', 'cambodia'))
