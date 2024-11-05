#8/10 This exercise was pretty challenging to write out but it is very useful in the real world for websites to remember users. 
import json  # Import the json module to handle JSON data.

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'  # Define the filename to store the username
    try:
        # Attempt to open the file and load the username.
        with open(filename) as f_obj:
            username = json.load(f_obj)  # Load the username from the JSON file.
    except FileNotFoundError:
        return None  # If the file is not found, return None.
    else:
        return username  # Return the stored username.

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")  # Ask the user for their name
    filename = 'username.json'  
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)  # Write the username to the file in JSON format.
    return username  # Return the new username.

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()  # Retrieve username.
    if username:
        # If a username is found, ask if it's correct.
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")  
        else:
            username = get_new_username() 
            print(f"We'll remember you when you come back, {username}!")
    else:
        # If no username is found, prompt for a new one.
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

# Call the function to greet the user.
greet_user()