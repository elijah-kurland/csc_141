def show_messages(messages):
    """Print all messages in the list."""
    
    print("Showing all messages:")
    
    # Loop through each message and print it.
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    
    # Print a header for sending messages.
    print("\nSending all messages:")
    
    # While there are messages in the original list, pop the last message,.
    while messages:
        current_message = messages.pop()  # Removes the last message from 'messages'.
        print(current_message)
        sent_messages.append(current_message)  # Adds the removed message to 'sent_messages'.

# A list of messages to show.
messages = ["Hello!", "How are you?", "Got any plans?"]

# Call the function to show the messages.
show_messages(messages)

# An empty list to store sent messages.
sent_messages = []

# Call the function to send messages and move them to 'sent_messages'.
# Using messages[:] to pass a copy of the original list.
send_messages(messages[:], sent_messages)

# Print the final state of both lists to verify the changes.
print("\nFinal lists:")
print(messages)        
print(sent_messages)   