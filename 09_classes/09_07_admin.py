class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, address):
        """Initialize the user."""
        self.first_name = first_name.title()  # Store the user's first name.
        self.last_name = last_name.title()    # Store the user's last name.
        self.username = username              # Store the user's username
        self.email = email                    # Store the user's email address.
        self.address = address.title()        # Store the user's address.
        self.login_attempts = 0               # Initialize login attempts to 0.

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Address: {self.address}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1 # Increase login attempts by 1.

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0 # Reset login attempts to 0.


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, address):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, address) # Initialize attributes from User.
        self.privileges = [] # Initialize an empty list to store admin privileges.

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}") # Display each privilege in the list.

# Create an instance of the Admin class.
elijah = Admin('elijah', 'kurland', 'e_kurland', 'e_kurland@gmail.com', 'coatesville')
elijah.describe_user() # Display user information.

# Define privileges for the admin user.
elijah.privileges = [
    'can add posts',
    'can delete posts',
    'can ban users',
]
# Display the admin's privileges.
elijah.show_privileges()