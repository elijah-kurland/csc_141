def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    
    # Output a message summarizing the shirt's size.
    print(f"\nI'm going to make a {size} t-shirt.")
    
    # Output the message that will be printed on the shirt.
    print(f'It will say, "{message}"')

# Call the function with positional arguments
make_shirt('small', 'Python Power!')

# Call the function with keyword arguments (order doesn't matter).
make_shirt(message="Game on!", size='medium')