class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title() # Store the restaurant's name.
        self.cuisine_type = cuisine_type # Store the type of food served.

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves {self.cuisine_type}."
        print(f"\n{msg}")  

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open!"
        print(f"\n{msg}") 

# Create an instance of the Restaurant class.
restaurant = Restaurant('Olive Garden', 'Italian food')

# Print the restaurant's name and cuisine type attributes.
print(restaurant.name)
print(restaurant.cuisine_type)

# Call the methods to display information about the restaurant.
restaurant.describe_restaurant()
restaurant.open_restaurant()