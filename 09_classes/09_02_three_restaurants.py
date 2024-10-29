class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title() # Store the restaurant's name.
        self.cuisine_type = cuisine_type # Store the type of food.

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves {self.cuisine_type}."
        print(f"\n{msg}") 

# Create instances of the Restaurant class.
olive_garden = Restaurant('Olive Garden', 'Italian food')
olive_garden.describe_restaurant()  

plaza_aztecka = Restaurant("Plaza Aztecka", 'Mexican food')
plaza_aztecka.describe_restaurant()  

zing = Restaurant('Zing', 'Asian food')
zing.describe_restaurant()  
