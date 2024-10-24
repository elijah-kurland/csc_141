def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    
    # Create a dictionary with the artist and album title, using title case.
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    
    # Return the dictionary.
    return album_dict