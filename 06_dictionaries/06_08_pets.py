#Creates an empty dictionary.
pets = []

#Creates a dictionary for the pet and adds it to the list.
pet = {
    'animal': 'cat',
    'name': 'Gingerbread',
    'owner': 'Elijah',
    'color': 'brown and white',
}
pets.append(pet)  # Append the pet dictionary to the list

pet = {
    'animal': 'dog',
    'name': 'Max',
    'owner': 'Elijah',
    'color': 'black',
}
pets.append(pet) 

pet = {
    'animal': 'russian tortoise',
    'name': 'Shelby',
    'owner': 'Elijah',
    'color': 'brown',
}
pets.append(pet) 

#Loops through each pet in the list to print their information.
for pet in pets:
    #Print the pet's information.
    print(f"\nInformation on {pet['name'].title()}:")
    
    #Loops through each key-value pair in the pet's dictionary.
    for key, value in pet.items():
        #Prints the key and its corresponding value.
        print(f"\t{key}: {value}")