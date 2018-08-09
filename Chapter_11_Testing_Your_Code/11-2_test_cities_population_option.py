import unittest
from city_function_add_population import get_formatted_city

class CitiesTestCase(unittest.TestCase):
	"""Tests for 'city_function_add_population.py'"""
	
	def test_city_and_county(self):
		"""Do city and county like 'San Diego, San Diego' work?"""
		formatted_city = get_formatted_city('San Diego', 'San Diego')
		self.assertEqual(formatted_city, "San Diego, San Diego")
	
	def test_city_county_population(self):
		"""Do city, county, and county population like 'San Diego, San Diego - population 3300000"""
		formatted_city = get_formatted_city('San Diego', 'San Diego' ,'3300000')
		self.assertEqual(formatted_city, "San Diego, San Diego - population 3300000")
	
unittest.main()