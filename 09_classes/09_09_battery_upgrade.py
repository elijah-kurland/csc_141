class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer  # Store the car's manufacturer.
        self.model = model                # Store the car's model.
        self.year = year                  # Store the car's manufacturing year.
        self.odometer_reading = 0         # Initialize odometer reading to 0.
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}" # Format name with year, manufacturer, and model.
        return long_name.title() # Return the name.
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")  
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading: # Check if the new mileage is greater than or equal to the current reading.
            self.odometer_reading = mileage  
        else:
            print("You can't roll back an odometer!") # Reject any attempt to roll back the odometer.
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles # Increment the odometer reading by the specified miles.

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size # Set the battery size.

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.") # Display the battery size.

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:  
            range = 260  
        elif self.battery_size == 100:
            range = 315 
            
        message = f"This car can go approximately {range}" # Create message with range.
        message += " miles on a full charge." # Add to message about full charge.
        print(message) # Display the range message.

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 75: # Check if the current battery size is 75 kWh.
            self.battery_size = 100 # Upgrade the battery to 100 kWh.
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.") # Inform that the battery is already at maximum capacity.
    
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year) # Initialize attributes from the parent Car class.
        self.battery = Battery() # Create an instance of Battery for the electric car.

# Create an instance of ElectricCar and check its range
print("Make an electric car, and check the range:")
my_tesla = ElectricCar('tesla', 'model s', 2024) # Instantiate an electric car object.
my_tesla.battery.get_range() # Call the method to check the range.

# Upgrade the battery and check the range again.
print("\nUpgrade the battery, and check the range again:")
my_tesla.battery.upgrade_battery() # Call the method to upgrade the battery.
my_tesla.battery.get_range() # Call the method again to check the new range.