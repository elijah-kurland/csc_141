class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()          # Store the restaurant's name.
        self.cuisine_type = cuisine_type  # Store the type of cuisine served.
        self.number_served = 0            # Initialize number of customers served to 0.

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves {self.cuisine_type}."
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served # Set number_served to specified value.

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served # Add to the existing number_served.


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type) # Initialize attributes from the Restaurant class.
        self.flavors = [] # Initialize an empty list to hold available flavors.

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}") # Display each flavor.

# Create an instance of the IceCreamStand class.
bells = IceCreamStand('Bells')
bells.flavors = ['vanilla', 'chocolate', 'strawberry'] # Set available flavors.

bells.describe_restaurant() # Display information about the ice cream stand.
bells.show_flavors()        # Show available ice cream flavors.