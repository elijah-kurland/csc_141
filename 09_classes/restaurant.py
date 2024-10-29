# Part of 09_10.
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant with its name and cuisine type."""
        self.name = name.title() # Store the restaurant's name.
        self.cuisine_type = cuisine_type # Store the type of cuisine served.
        self.number_served = 0 # Initialize the number of customers served to zero.

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}." # Create message.
        print(f"\n{msg}") # Print message.

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!" # Create message.
        print(f"\n{msg}") # Print message.

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served # Update the number served with the given value.

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served # Increase the number served by the additional amount.