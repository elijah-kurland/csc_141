class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()             # Store the restaurant's name.
        self.cuisine_type = cuisine_type     # Store the type of food served.
        self.number_served = 0               # Initialize number of customers served to 0.

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served  # Set number_served to specified value.

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served  # Add to the existing number_served.

# Create an instance of the Restaurant class.
restaurant = Restaurant('the Olive Garden', 'Italian food')
restaurant.describe_restaurant()

# Display initial number of customers served.
print(f"\nNumber served: {restaurant.number_served}")

# Directly modify the number_served attribute.
restaurant.number_served = 130
print(f"Number served: {restaurant.number_served}")

# Use set_number_served() method to set a new number of customers served.
restaurant.set_number_served(501)
print(f"Number served: {restaurant.number_served}")
