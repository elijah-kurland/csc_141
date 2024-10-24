import printing_functions as pf  # Importing the custom module for printing functions.

# List of designs that have not been printed yet.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']

# List to store completed models.
completed_models = []

# Call the function to print the models and move them to completed models.
pf.print_models(unprinted_designs, completed_models)

# Call the function to display the completed models.
pf.show_completed_models(completed_models)