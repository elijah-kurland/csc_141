#Assigns alien color variable.
alien_color = 'green'

#Check the color of the alien and assign points based on the color.
if alien_color == 'green':
    print("You earned 5 points!") 
elif alien_color == 'yellow':
    print("You earned 10 points!") 
else:
    print("You earned 15 points!") 
    alien_color = 'red'  #Change alien color to red.

#Change the alien color to yellow for the next check.
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

    alien_color = 'red'  #Change alien color to red.

#Check the color of the alien again.
if alien_color == 'green':
    print("You earned 5 points!")  
elif alien_color == 'yellow':
    print("You earned 10 points!") 
else:
    print("You earned 15 points!") 