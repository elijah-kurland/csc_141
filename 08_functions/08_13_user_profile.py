def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    
    # Add first and last name to the user_info dictionary.
    user_info['first_name'] = first
    user_info['last_name'] = last
    
    # Return the complete user profile dictionary.
    return user_info

# Call the function to build a user profile with additional information.
user_profile = build_profile('Elijah', 'Kurland',
                             location='Albright',
                             field='Game and Sim',
                             hobby='photography')

# Print the resulting user profile.
print(user_profile)