import album_functions as af  # Import the album_functions module with an alias.

# Call the function for different albums and print the results.
album = af.make_album('CHVCHES', 'Screen Violence')
print(album)

album = af.make_album('Noah Kahan', 'Stick Season')
print(album)

album = af.make_album('Florence and The Machine', 'Lungs') 
print(album)



from album_functions import make_album  # Import the make_album function directly.

# Call the function for different albums and print the results.
album = make_album('CHVCHES', 'Screen Violence')
print(album)

album = make_album('Noah Kahan', 'Stick Season')
print(album)

album = make_album('Florence and The Machine', 'Lungs')
print(album)



from album_functions import make_album as fn  # Import the make_album function with an alias.

# Call the function for different albums and print the results.
album = fn('CHVCHES', 'Screen Violence')  
print(album)

album = fn('Noah Kahan', 'Stick Season')  
print(album)

album = fn('Florence and The Machine', 'Lungs')  
print(album)



import album_functions as mn  # Import the album_functions module with an alias.

# Call the function for different albums and print the results.
album = mn.make_album('CHVCHES', 'Screen Violence') 
print(album)

album = mn.make_album('Noah Kahan', 'Stick Season')  
print(album)

album = mn.make_album('Florence and The Machine', 'Lungs')  
print(album)



from album_functions import *  # Import all functions and variables from the album_functions module.

# Call the function for different albums and print the results.
album = make_album('CHVCHES', 'Screen Violence')  
print(album)

album = make_album('Noah Kahan', 'Stick Season')  
print(album)

album = make_album('Florence and The Machine', 'Lungs')  
print(album)