#4/10 This code was simple to write and understand as how to store certain attributes. 
class Employee():
    """A class to represent an employee."""

    def __init__(self, f_name, l_name, salary):
        """Initialize the employee with first name, last name, and salary."""
        self.first = f_name.title() # Store the first name.
        self.last = l_name.title()  # Store the last name.
        self.salary = salary        # Store the salary.

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount  # Increase the salary by the specified amount.