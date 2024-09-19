#This prints the list of animals.
animals = ['Goldfish', 'Betafish', 'Pufferfish']
for animal in animals:
    print (animal)

print("\n")

#This prints the list but adds a personal message to each item.
for animal in animals:
    print(f"My favourite fish are {animal.title()}.")
    
#This prints a single line of the sentence.
print("\nAll of these animals are types of fish.")