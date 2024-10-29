# Part of 09_11.
from user import Admin # Import the Admin class from the user module.

# Create an instance of the Admin class for a user named Elijah.
elijah = Admin('elijah', 'kurland', 'e_kurland', 'e_kurland@gmail.com', 'coatesville')

# Display the user's information by calling the describe_user method.
elijah.describe_user()

# Define a list of privileges that the admin has.
elijah_privileges = [
    'can add posts',    # Privilege to add new posts.
    'can delete post',  # Privilege to delete existing posts.
    'can ban user',     # Privilege to ban users from the platform.
]
# Assign the list of privileges to the admin's privileges attribute.
elijah.privileges.privileges = elijah_privileges

# Print the privileges associated with the admin.
print(f"\nThe admin {elijah.username} has these privileges: ")
elijah.privileges.show_privileges() # Call the method to display the admin's privileges.