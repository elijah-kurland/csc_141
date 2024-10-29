# Part of 09_12.
from admin import Admin # Import the Admin class from the admin module.

# Create an instance of Admin.
elijah = Admin('elijah', 'kurland', 'e_kurland', 'e_kurland@gmail.com', 'coatesville')

# Display user information.
elijah.describe_user()

# Define a list of privileges for the admin.
elijah_privileges = [
    'can add posts',
    'can delete post',
    'can ban user',
]

# Assign the defined privileges to the admin's privileges attribute.
elijah.privileges.privileges = elijah_privileges

# Print the admin's privileges.
print(f"\nThe admin {elijah.username} has these privileges: ")
elijah.privileges.show_privileges() # Show the privileges associated with the admin.
