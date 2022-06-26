pizzas = ['vegetarian', 'combination', 'pepperoni']
for pizza in pizzas:
    print(f"I like {pizza} pizza\n")

print(f"I REALLY LOVE PIZZZAA!\n")

animals = ['cat', 'spider', 'hungarian horntail']
for animal in animals:
    print(f"A {animal} would make a fantastic pet\n")

print(f"Any of these animals would be a perfect, or possibly not so perfect pet.")


#####copies list with all original items#####
friend_pizza = pizzas[:]

#####adds item to original list#####
pizzas.append('stuffed crust')
friend_pizza.append('anchovies')

print("\nMy favorite pizza is:")
print(pizzas)

print("\nMy friend's favorite pizza is:")
print(friend_pizza)

