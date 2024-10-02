#Creates a dictionary to store information about different aliens.
aliens = {
    'alien_0': {
        'color': 'green',
        'points': 3,
        'speed': 'slow',
        'difficulty': 'easy',
    },
    'alien_1': {
        'color': 'blue',
        'points': 5,
        'speed': 'normal',
        'difficulty': 'medium',
    },
    'alien_2': {
        'color': 'red',
        'points': 10,
        'speed': 'fast',
        'difficulty': 'hard',
    },
} 

#Loops through each alien and its corresponding information.
for alien, info in aliens.items():
    #Extracts the alien's information.
    color = info['color'].title()           
    points = info['points']                  
    speed = info['speed'].title()            
    difficulty = info['difficulty'].title()  

    #Prints information about the alien.
    print(f"\n{alien.title()} is {color}.")
    print(f"This alien rewards {points} points.")
    print(f"It's speed is {speed}.")
    print(f"The alien's difficulty is {difficulty}.")

#Final prompt to the player.
print("\nCan you defeat all of the aliens?")