#Creates an empty dictionary.
people = []

#Creates a dictionary for the person and adds them to the list.
person = {
    'first_name': 'Ryan',
    'last_name': 'Cooper',
    'age': '19',
    'city': 'Oxford',
}
people.append(person)  #Append the person dictionary to the list.

person = {
    'first_name': 'Avery',
    'last_name': 'Merrit',
    'age': '18',
    'city': 'Downingtown',
}
people.append(person) 

person = {
    'first_name': 'Joren',
    'last_name': 'Deo',
    'age': '18',
    'city': 'Downingtown',
}
people.append(person)  

#Loop through each person in the list to print their information.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    #Gets the age from the person's dictionary.
    age = f"{person['age']}"
    #Gets the city from the person's dictionary.
    city = f"{person['city']}"

    #Prints a string with the person's information.
    print(f"{name}, of {city}, is {age} years old.")