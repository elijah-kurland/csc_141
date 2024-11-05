#3/10 This exercise was pretty simple and actually fun to make.
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    # Ask the user for their name.
    name = input("\nWhat's your name? ")
    
    # Check if the user wants to quit.
    if name == 'quit':
        break
    else:
        # Open the file in append mode and add the name with a newline.
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        
        # Confirm the addition to the guest book.
        print(f"Hi {name}, you've been added to the guest book.")