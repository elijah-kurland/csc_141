#9/10 I did not understand this exercise and had to use chat to help. I wrote the code but didn't really understand unittest.
# This is the final version of 11_02 Population.
import unittest  # Import the unittest module for testing.

from city_functions import city_country  # Import the city_country function from city_functions module.

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        # Call the function with city and country and store the result.
        santiago_chile = city_country('tokyo', 'japan')
        # Check if the result matches the expected output.
        self.assertEqual(santiago_chile, 'Tokyo, Japan')

    def test_city_country_population(self):
        """Can I include a population argument?"""
        # Call the function with city, country, and population and store the result.
        santiago_chile = city_country('tokyo', 'japan', population=14_000_000)

        # Check if the result matches the expected output
        self.assertEqual(santiago_chile, 'Tokyo, Japan - population 14000000')

# If this module is run directly, execute the test cases.
if __name__ == '__main__':
    unittest.main()