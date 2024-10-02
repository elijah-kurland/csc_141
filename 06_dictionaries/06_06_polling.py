#Create a dictionary that stores names and their favorite programming language.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#Checks for names that are in the dictionary and prints the according message.
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

#List of people who might have taken the poll.
people = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

#Loops through each person in the list.
for person in people:
    #Checks if the person's name is a key in the favorite_languages dictionary.
    if person in favorite_languages.keys():
        #Thanks the people that took the poll.
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        #Instructs those who did not take the poll to do so.
        print(f"{person.title()}, please take the poll.")