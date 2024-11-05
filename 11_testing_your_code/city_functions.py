#3/10 This exercise required a previous code but was very simple to understand.
"""A collection of functions for working with cities."""  

def city_country(city, country, population):

    # Create a formatted string with the city and country.
    output_string = f"{city.title()}, {country.title()}"

    # Append the population information to the string.
    output_string += f" - population {population}"

    return output_string  # Return the formatted string.