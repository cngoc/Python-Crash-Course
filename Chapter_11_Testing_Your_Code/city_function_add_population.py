def get_formatted_city(city, county, population = ''):
	"""Generate a neatly formatted city and county"""
	if population:
		full_city = city.title() + ', ' + county.title() + ' - population ' + population
	else:
		full_city = city + ', ' + county
	return full_city