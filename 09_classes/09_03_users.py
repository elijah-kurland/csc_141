class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, address):
        """Initialize the user."""
        self.first_name = first_name.title()  # Store the user's first name.
        self.last_name = last_name.title()    # Store the user's last name.
        self.username = username              # Store the user's username.
        self.email = email                    # Store the user's email address.
        self.address = address.title()        # Store the user's address.

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Address: {self.address}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

# Create instances of the User class.
elijah = User('elijah', 'kurland', 'e_kurland', 'e_kurland@gmail.com', 'coatesville')
elijah.describe_user() # Display information for user.
elijah.greet_user()    # Greet user.

joren = User('joren', 'deo', 'j_deo', 'j_deo@gmail.com', 'downingtown')
joren.describe_user()   
joren.greet_user()      
