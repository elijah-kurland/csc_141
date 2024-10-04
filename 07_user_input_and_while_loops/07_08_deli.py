#List of sandwich orders to process.
sandwitch_orders = ['grilled cheese', 'BLT', 'veggie']
#List to keep track of finished sandwiches.
finished_sandwitches = []

#Loop until there are no more sandwich orders.
while sandwitch_orders:
    #Remove the last sandwich order from the list and store it in 'current_sandwitch'.
    current_sandwitch = sandwitch_orders.pop()
    
    #Print a message indicating the current sandwich being prepared.
    print("I'm working on your " + current_sandwitch + " sandwich.")
    
    #Add the finished sandwich to the 'finished_sandwitches' list.
    finished_sandwitches.append(current_sandwitch)

print("\n")

#Loop through the list of finished sandwiches and print each one.
for sandwitch in finished_sandwitches:
    print("I made a " + sandwitch + " sandwich.")