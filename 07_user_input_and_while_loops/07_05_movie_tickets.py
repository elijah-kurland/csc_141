#Initialize the prompt for asking the user's age.
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are done:"

#Start an infinite loop to collect ages.
while True:
    #Get user input for age.
    age = input(prompt)
    
    #Check if the user wants to quit the input process.
    if age == 'quit':
        break
    
    #Convert the input to an integer.
    age = int(age)

    #Determine ticket price based on age.
    if age < 3:
        print("You get in free.")  
    elif age < 13:
        print("Your ticket is $10.")  
    else:
        print("Your ticket is $15.") 