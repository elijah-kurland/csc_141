#This prints the list of pizzas.
pizzas = ['plain', 'margarita', 'white']
for pizza in pizzas:
    print(pizza)

print("\n")

#Prints the same list but adds the message.
for pizza in pizzas:
    print(f"I really love {pizza.title()}.")
    
#prints separately from the list as a single sentence.
print("\nI really love pizza.")