#Create a dictionary that stores rivers and the country the belong in.
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    }

#Print the location of each river.
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

#Prints all river names within the data set.
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

#Prints all country names within the data set.
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")