#4/10 This exercise was pretty straight forward and useful.
try:
    # Prompt the user for a number and convert the input to an integer.
    x = input("Give me a number: ")
    x = int(x)

    # Prompt the user for another number and convert the input to an integer.
    y = input("Give me another number: ")
    y = int(y)

# Handle the case where the input is not a valid integer.
except ValueError:
    print("Sorry, I really needed a number.")

# If no exception occurs, execute the following code block.
else:
    sum = x + y

    print(f"The sum of {x} and {y} is {sum}.")
