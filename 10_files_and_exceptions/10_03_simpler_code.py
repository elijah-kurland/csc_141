#3/10 This exercise was pretty simple and easy to understand.
# Ask the user for their name.
name = input("What's your name? ")

# Define the filename to store the guest's name.
filename = 'guest.txt'

# Open the file in write mode and save the name.
with open(filename, 'w') as f:
    f.write(name)
