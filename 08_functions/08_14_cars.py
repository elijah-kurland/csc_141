def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    
    # Create a dictionary with the manufacturer and model of the car.
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    
    # Loop through any additional options and add them to the car dictionary.
    for option, value in options.items():
        car_dict[option] = value

    # Return the completed car dictionary.
    return car_dict

# Create a car dictionary with specific options.
my_honda = make_car('honda', 'odyssey', color='blue', adjustable_side_mirrors=True)
print(my_honda)

# Create a car dictionary with specific options.
my_tesla = make_car('tesla', 'cybertruck', year=1991, color='silver', reclining_seats=True)
print(my_tesla)