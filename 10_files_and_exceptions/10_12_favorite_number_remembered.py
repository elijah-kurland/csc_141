#7/10 This exercise was challenging somewhere in between the last two.
import json  # Import the json module to work with JSON data.

try:
    # Attempt to open the JSON file and load the favorite number.
    with open('favorite_number.json') as f:
        number = json.load(f)

# Handle the case where the file is not found.
except FileNotFoundError:
    # If the file doesn't exist, prompt the user for their favorite number.
    number = input("What's your favorite number? ")
    
    # Open the file in write mode to save the user's favorite number.
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)  # Write the number to the file in JSON format.
    
    print("Thanks, I'll remember that.")

# If the file was found and read successfully, print the favorite number.
else:
    print(f"I know your favorite number! It's {number}.")