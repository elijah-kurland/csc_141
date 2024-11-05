#8/10 This exercise introduced me to json files and took a bit to understand. It also wouldn't run unless I ran a previous file.
import json  # Import the json module to work with JSON data.

# Open the JSON file and load its content.
with open('favorite_number.json') as f:
    number = json.load(f)  # Load the JSON data into the variable 'number'.

# Print a message revealing the user's favorite number.
print(f"I know your favorite number! It's {number}.")