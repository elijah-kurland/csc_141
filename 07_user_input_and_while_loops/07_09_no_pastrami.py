#List of sandwich orders, including multiple 'pastrami' orders.
sandwitch_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'BLT', 'turkey', 'pastrami'
]
#List to keep track of finished sandwiches.
finished_sandwitches = []

#Inform the customer that 'pastrami' is out of stock.
print("I'm sorry, we are out of pastrami.")

#Remove all instances of 'pastrami' from the sandwich orders.
while 'pastrami' in sandwitch_orders:
    sandwitch_orders.remove('pastrami')

print("\n") 

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
    print("I made you a " + sandwitch + " sandwich.")