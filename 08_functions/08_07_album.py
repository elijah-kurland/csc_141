def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    
    # Create a dictionary with the artist and album title, using title case.
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    
    # Return the dictionary.
    return album_dict

# Call the function for the album and print the result.
album = make_album('CHVCHES', 'Screen Violence')
print(album)

album = make_album('Noah Kahan', 'Stick Season')
print(album)

album = make_album('Florance and The Machine', 'Lungs')
print(album)