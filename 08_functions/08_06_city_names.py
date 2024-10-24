def city_country(city, country):
    """Return a string formatted like 'Santiago, Chile'."""
    
    # Return the city and country formatted as 'City, Country' with title casing.
    return f"{city.title()}, {country.title()}"

# Call the function and print the result.
city = city_country('santiago', 'chile')
print(city)

city = city_country('chicago', 'united states')
print(city)

city = city_country('tokyo', 'japan')
print(city)