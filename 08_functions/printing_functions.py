"""Functions related to printing 3D models."""

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until there are none left.
    Move each design to completed_models after printing.
    """
    # Continue the process until there are no unprinted designs left
    while unprinted_designs:
        # Remove the last design from the unprinted designs list
        current_design = unprinted_designs.pop()
    
        # Simulate printing the current design
        print(f"Printing model: {current_design}")
        
        # Add the printed design to the completed models list
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    
    # Loop through the completed models and print each one
    for completed_model in completed_models:
        print(completed_model)