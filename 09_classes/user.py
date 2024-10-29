# Part of 09_11.
"""A collection of classes for modeling users."""

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, address):
        """Initialize the user with personal details."""
        self.first_name = first_name.title() 
        self.last_name = last_name.title()   
        self.username = username            # Store the username.
        self.email = email                  # Store the email address.
        self.address = address.title()      # Capitalize the address.
        self.login_attempts = 0             # Initialize login attempts to zero.

    def describe_user(self):
        """Display a summary of the user's information."""
        # Print the user's full name and details.
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Address: {self.address}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        # Greet the user using their username.
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1 # Increase the count of login attempts.

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0 # Set login attempts back to zero.


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, address):
        """Initialize the admin with personal details and privileges."""
        super().__init__(first_name, last_name, username, email, address) # Call the parent class constructor.
        
        # Initialize an empty set of privileges for the admin user.
        self.privileges = Privileges() # Create an instance of Privileges.


class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        """Initialize privileges, with an optional list of privileges."""
        self.privileges = privileges # Store the privileges of the admin.

    def show_privileges(self):
        """Display the list of privileges for the admin."""
        print("\nPrivileges:") # Heading for the privilege list.
        if self.privileges: # Check if there are any privileges.
            for privilege in self.privileges: # Iterate through the privileges.
                print(f"- {privilege}") # Print each privilege.
        else:
            print("- This user has no privileges.") # Message if no privileges are set.