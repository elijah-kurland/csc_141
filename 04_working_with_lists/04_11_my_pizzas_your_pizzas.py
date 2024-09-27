pizzas = ['Plain', 'Margarita', 'White']
friend_pizzas = pizzas[:]

#This adds these two items to the repected lists.
pizzas.append('tommato_pie')
friend_pizzas.append('Pesto')

#This prints the updated list.
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f'- {pizza}')
    
#This prints the updated list.
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f'-{pizza}')
