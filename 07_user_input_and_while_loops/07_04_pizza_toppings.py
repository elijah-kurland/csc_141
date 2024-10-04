#Initialize the prompt for asking about pizza toppings.
prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\nEnter 'quit' when you are done:"

#Start an infinite loop to collect pizza toppings.
while True:
    topping = input(prompt)
    
    #Check if the user wants to quit the input process.
    if topping != 'quit':
        #Adds topping to pizza.
        print("I'll add " + topping + " to your pizza.")
    else:
        #Exit the loop if the user types 'quit'.
        break