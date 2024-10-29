class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, address):
        """Initialize the user."""
        self.first_name = first_name.title()  # Store the user's first name.
        self.last_name = last_name.title()    # Store the user's last name.
        self.username = username              # Store the user's username.
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
        self.login_attempts += 1  # Increase login attempts by 1.

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0   # Reset login attempts to 0.

# Create an instance of the User class.
elijah = User('elijah', 'kurland', 'e_kurland', 'e_kurland@gmail.com', 'coatesville')
elijah.describe_user()  # Display user.
elijah.greet_user()     # Greet user.

# Simulate multiple login attempts.
print("\nMaking 3 login attempts...")
elijah.increment_login_attempts()
elijah.increment_login_attempts()
elijah.increment_login_attempts()
print(f"  Login attempts: {elijah.login_attempts}") # Display current login attempts.

# Reset login attempts.
print("Resetting login attempts...")
elijah.reset_login_attempts()
print(f"  Login attempts: {elijah.login_attempts}") # Confirm login attempts are reset.