#Creates a dictionary to store information about cities.
cities = {
    'New York': {
        'country': 'United States',
        'population': 8_000_000,
        'fact': 'The first pizzeria in the US appeared in New York.',
    },
    'Anaheim': {
        'country': 'United States',
        'population': 350_000,
        'fact': 'Home to Disneyland.',
    },
    'Chicago': {
        'country': 'United States',
        'population': 2_700_000,
        'fact': 'The first skyscraper was built in Chicago.',
    }
} 

#Loops through each city and its corresponding information.
for city, info in cities.items():
    #Extracts country, population, and fact.
    country = info['country'].title()  
    population = info['population']      
    facts = info['fact'].title()        

    #Prints information about the cities.
    print(f"\n{city.title()} is in the {country}.")
    print(f"It has a population of about {population}.")
    print(f"{facts}")