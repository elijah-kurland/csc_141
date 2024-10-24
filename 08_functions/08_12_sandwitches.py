def make_sandwich(*items):
    """Make a sandwich with the given items."""
    
    # Print a header for the sandwich-making process.
    print("\nI will make you a sandwich:")
    
    # Loop through each item and print what will be added to the sandwich.
    for item in items:
        print(f"I will add {item} to your sandwich.")
    
    # Print a final message indicating the sandwich is ready.
    print("Your sandwich is now ready!")

# Call the function with different sets of sandwich ingredients.
make_sandwich('american cheese', 'tomato', 'lettuce', 'mayo')
make_sandwich('cheddar', 'avocado', 'ranch')
make_sandwich('peanut butter', 'jelly')