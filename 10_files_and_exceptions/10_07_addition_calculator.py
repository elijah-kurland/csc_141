#6/10 This exercise seemed to be similar to the last but with more lines of code. I am still a little unsure of how they are different. 
print("Enter 'q' at any time to quit.\n")

# Start an infinite loop to repeatedly ask for input.
while True:
    try:
        # Ask the user for the first number.
        x = input("\nGive me a number: ")
        
        # Check if the user wants to quit.
        if x == 'q':
            break

        # Convert the input to an integer.
        x = int(x)

        y = input("Give me another number: ")
        
        if y == 'q':
            break

        y = int(y)

    # Handle the case where the input is not a valid integer.
    except ValueError:
        print("Sorry, I really needed a number.")

    # If no exception occurs, calculate and display the sum.
    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")