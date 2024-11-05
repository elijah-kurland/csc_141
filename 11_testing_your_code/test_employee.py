#7/10 This exercise was verry challenging but was easier to understand after doing the last code.
import unittest  # Import the unittest module for testing.

from employee import Employee  # Import the Employee class from the employee module.

class TestEmployee(unittest.TestCase):
    """Tests for the module employee."""

    def setUp(self):
        """Make an employee to use in tests."""
        # Create an instance of Employee for testing purposes.
        self.elijah = Employee('eric', 'matthes', 65_000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        # Call the give_raise method without arguments.
        self.eric.give_raise()
        # Check if the salary was updated correctly.
        self.assertEqual(self.elijah.salary, 70000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        # Call the give_raise method with a custom raise amount.
        self.elijah.give_raise(10000)
        # Check if the salary was updated correctly.
        self.assertEqual(self.elijah.salary, 75000)

# If this module is run directly, execute the test cases.
if __name__ == '__main__':
    unittest.main()