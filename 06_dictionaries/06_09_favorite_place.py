#Creates a dictionary to store favorite places for different people.
favorite_places = {
    'Elijah': ['Iceland', 'Disney', 'Japan'],
    'Ava': ['Paris', 'Hawaii', 'Canada'], 
    'Joren': ['The Philippines', 'Japan', 'Ireland'],
}

#Loops through each person's name and their list of favorite places.
for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following:")
    
    #Loops through the list of places for the current person.
    for place in places:
        #Prints each favorite place.
        print(f"{place.title()}")