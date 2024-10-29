from random import choice # Import the choice function from the random module.

# Define the possible values for the winning ticket.
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Initialize an empty list to hold the winning ticket numbers/characters.
winning_ticket = []
print("What is the winning ticket?") 

# Continue until we have 4 unique items in the winning ticket.
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities) # Randomly select an item.

    # Check if the pulled item is already in the winning ticket.
    if pulled_item not in winning_ticket:
        print(f"  We pulled a {pulled_item}!") 
        winning_ticket.append(pulled_item) # Add the item to the winning ticket.