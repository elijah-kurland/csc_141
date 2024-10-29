# Part of 09_12.
"""A class for modeling users."""

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, address):
        """Initialize the user with personal information."""
        self.first_name = first_name.title()  
        self.last_name = last_name.title()   
        self.username = username            # Store the username.
        self.email = email                  # Store the email address.
        self.address = address.title()      # Capitalize the address.
        self.login_attempts = 0             # Initialize login attempts to zero.

    def describe_user(self):
        """Display a summary of the user's information."""
        # Print the user's full name and other details.
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Address: {self.address}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        # Greet the user by their username.
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1 # Increase the count of login attempts.

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0 # Set the number of login attempts back to zero.