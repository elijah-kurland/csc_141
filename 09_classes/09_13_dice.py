from random import randint # Import the randint function from the random module.

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die with a default number of sides."""
        self.sides = sides # Set the number of sides for the die.

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        return randint(1, self.sides) # Roll the die and return the result.

# Create a 6-sided die.
d6 = Die()

# Roll the 6-sided die 10 times and store the results. 
results = []
for roll_num in range(10):
    result = d6.roll_die()  
    results.append(result) # Append the result to the results list.

# Print the results of the 6-sided die rolls.
print("10 rolls of a 6-sided die:")
print(results)

# Create a 10-sided die.
d10 = Die(sides=10)

# Roll the 10-sided die 10 times and store the results.
results = []
for roll_num in range(10):
    result = d10.roll_die() 
    results.append(result) # Append the result to the results list.

# Print the results of the 10-sided die rolls.
print("\n10 rolls of a 10-sided die:")
print(results)

# Create a 20-sided die.
d20 = Die(sides=20)

# Roll the 20-sided die 10 times and store the results.
results = []
for roll_num in range(10):
    result = d20.roll_die() 
    results.append(result) # Append the result to the results list.

# Print the results of the 20-sided die rolls.
print("\n10 rolls of a 20-sided die:")
print(results)
