#Creates a tuple of current users.
current_users = ('Chris', 'Joren', 'Ryan', 'Martina', 'Bao')

#Creates a tuple of new users to check against current users.
new_users = ('ryan', 'Cydney', 'Tyler', 'Elijah', 'Cormac')

#Converts all current users to lowercase
current_users_lower = {user.lower() for user in current_users}

for new_user in new_users:
    #Checks if the new username (in lowercase) is already taken.
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")