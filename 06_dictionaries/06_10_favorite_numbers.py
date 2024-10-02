#Creates a dictionary to store favorite numbers for different people.
favorite_numbers = {
    'Ryan': ['36', '467', '382'],
    'Avery': ['92', '329', '282'],
    'Joren': ['27', '19', '390'],
    'Chris': ['82', '746', '832'],
    'Bao': ['43', '633', '272'],
}

#Loops through each person's name and their list of favorite numbers.
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the numbers:")
    
    #Loops through the list of numbers for the current person.
    for number in numbers:
        #Prints each favorite number.
        print(f"{number}")