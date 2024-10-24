def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    
    # Create a dictionary with the artist and album title, using title case.
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    
    # If the number of tracks is provided, add it to the dictionary.
    if tracks:
        album_dict['tracks'] = tracks
    
    # Return the completed album dictionary.
    return album_dict

# Prompts to ask the user for album and artist information.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit the program
print("Enter 'quit' at any time to stop.")

# Start an infinite loop to keep asking for input until the user quits.
while True:
    # Ask the user for the album title.
    title = input(title_prompt)
    
    # Check if the user wants to quit.
    if title.lower() == 'quit':
        break
    
    # Ask the user for the artist's name.
    artist = input(artist_prompt)
    
    if artist.lower() == 'quit':
        break

    # Call the make_album function and print the resulting dictionary.
    album = make_album(artist, title)
    print(album)

print("\nThank you!")