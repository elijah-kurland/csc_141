#6/10 This exercise continued with json files and was a bit easier to understand.
import json  # Import the json module to work with JSON data.

# Prompt the user for their favorite number.
number = input("What's your favorite number? ")

# Open the JSON file in write mode ('w') to save the favorite number.
with open('favorite_number.json', 'w') as f:
    # Write the user's favorite number to the file in JSON format.
    json.dump(number, f)
    
    print("Thanks! I'll remember that.")