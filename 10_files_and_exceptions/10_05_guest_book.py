#4/10 This exercise was similar to the last but with an extra step.
filename = 'programming_poll.txt'

# List to store responses.
responses = []

# Continuously prompt for responses.
while True:
    # Ask the user why they like programming.
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    # Ask if another person would like to respond.
    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

# Open the file in append mode and write each response on a new line.
with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")