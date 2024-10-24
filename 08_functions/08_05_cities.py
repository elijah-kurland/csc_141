def describe_city(city, country='United States'):
    """Describe a city."""
    
    # Create a message summarizing the city and its country.
    msg = f"{city.title()} is in {country.title()}."
    
    print(msg)

# Call the function for a city in the country.
describe_city('New York')

describe_city('reykjavik', 'iceland')

describe_city('Las Angeles')