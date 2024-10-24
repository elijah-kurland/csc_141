def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    
    # Output a message summarizing the shirt's size.
    print(f"\nI'm going to make a {size} t-shirt.")
    
    # Output the message that will be printed on the shirt.
    print(f'It will say, "{message}"')

# Call the function without arguments, using default size and message.
make_shirt()

# Call the function with a custom size.
make_shirt(size='medium')

make_shirt('small', 'Programming Rocks!')