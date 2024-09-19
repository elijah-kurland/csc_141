pizzas = ['Plain', 'Margarita', 'White']
friend_pizzas = pizzas[:]

pizzas.append('tommato_pie')
friend_pizzas.append('Pesto')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f'- {pizza}')

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f'-{pizza}')
