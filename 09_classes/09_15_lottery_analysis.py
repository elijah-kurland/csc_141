from random import choice # Import the choice function from the random module.

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = [] # Initialize an empty list for the winning ticket.

    # Loop until we have 4 unique items in the winning ticket.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities) # Randomly select an item from possibilities.

        # Only add the pulled item to the winning ticket if it hasn't already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item) # Add to winning ticket.

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    """Check if the played ticket matches the winning ticket."""
    # Check all elements in the played ticket.
    for element in played_ticket:
        # If any element is not in the winning ticket, return False.
        if element not in winning_ticket:
            return False

    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = [] # Initialize an empty list for the player's ticket.
    # Loop until we have 4 unique items in the ticket.
    while len(ticket) < 4:
        pulled_item = choice(possibilities) # Randomly select an item from possibilities.

        # Only add the pulled item to the ticket if it hasn't already been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item) # Add to player's ticket if unique.

    return ticket

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
# Get a winning ticket from the possibilities.
winning_ticket = get_winning_ticket(possibilities)

plays = 0 # Initialize the number of plays.
won = False # Initialize the win status.

# Set a maximum number of tries to prevent an infinite loop.
max_tries = 1_000_000

# Loop until a winning ticket is found or max tries is reached.
while not won:
    new_ticket = make_random_ticket(possibilities) # Create a new random ticket.
    won = check_ticket(new_ticket, winning_ticket) # Check if the new ticket is a winner.
    plays += 1 
    if plays >= max_tries:
        break 

# Output the results based on whether a winning ticket was found.
if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}") # Show the player's ticket.
    print(f"Winning ticket: {winning_ticket}") # Show the winning ticket.
    print(f"It only took {plays} tries to win!") # Show how many tries it took.
else:
    print(f"Tried {plays} times, without pulling a winner. :(") 
    print(f"Your ticket: {new_ticket}") 
    print(f"Winning ticket: {winning_ticket}") 