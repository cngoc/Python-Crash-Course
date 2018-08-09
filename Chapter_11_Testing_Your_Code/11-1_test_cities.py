import unittest
from city_function import get_formatted_city

class CitiesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'"""
	
	def test_city_and_county(self):
		"""Do city and county like 'San Diego, San Diego' work?"""
		formatted_city = get_formatted_city('San Diego', 'San Diego')
		self.assertEqual(formatted_city, "San Diego, San Diego")
		
unittest.main()