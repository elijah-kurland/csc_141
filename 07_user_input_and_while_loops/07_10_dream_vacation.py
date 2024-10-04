#Prompts for user input.
name_prompt = "\nWhat's your name?"
place_prompt = "Where would you visit in the world?"
question_prompt = "Would you like others to respond? (yes/no)"

#Dictionary to store responses.
responses = {}

#Start an infinite loop to collect user responses.
while True:
    #Get the user's name.
    name = input(name_prompt)
    #Get the place the user would like to visit.
    place = input(place_prompt)

    #Store the user's response in the dictionary with name as the key and place as the value.
    responses[name] = place

    #Ask if the user wants others to respond.
    repeat = input(question_prompt)
    #Exit the loop if the user answers anything other than 'yes'.
    if repeat.lower() != 'yes':
        break

print("\nResults:")
#Loop through the responses dictionary and print each name and their place.
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")