#Initialize the prompt for asking the user's age.
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are done:"

#Set the maximum number of iterations for the loop.
loop_duration = 5
current_iterations = 0  #Counter to track the number of iterations.

#Start an infinite loop to collect ages.
while True:
    #Check if the maximum number of iterations has been reached.
    if current_iterations >= loop_duration:
        print("Loop has reached the maximum allowed iterations.")
        break 

    #Get user input for age.
    age = input(prompt)
    
    #Check if the user wants to quit the input process.
    if age == 'quit':
        break 
    
    #Attempt to convert the input to an integer; handle errors if conversion fails.
    try:
        age = int(age)
    except ValueError:
        print("Please enter a valid age or 'quit' to exit.")
        continue  #Skip to the next iteration of the loop.

    #Determine ticket price based on age.
    if age < 3:
        print("You get in free.") 
    elif age < 13:
        print("Your ticket is $10.")  
    else:
        print("Your ticket is $15.")  
    
    current_iterations += 1  #Increment the iteration counter.