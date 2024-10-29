# Part of 09_12.
"""A collection of classes for modeling an admin user account."""

from user import User # Import the User class from the user module.

class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, address):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, address) # Initialize the base User class.
       
        # Initialize an empty set of privileges for the admin..
        self.privileges = Privileges() # Create a Privileges instance to store admin privileges.


class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        """Initialize the privileges list."""
        self.privileges = privileges # Store the list of privileges.

    def show_privileges(self):
        """Display the privileges of the admin."""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges: # Loop through and print each privilege.
                print(f"- {privilege}")
        else: 
            print("- This user has no privileges.") # Inform that the admin has no privileges.