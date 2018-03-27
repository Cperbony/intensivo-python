pizzas = ['calabreza', 'peperonni', 'Muzzarela']
for pizza in pizzas:
    print("I love pizza de " + pizza.title())
    print("I really love pizza de " + pizza.title() + "\n")

friends_pizzas = pizzas[:]
friends_pizzas.append('tortella')
print(friends_pizzas)

print()
print("Minhas pizzas favoritas são: " + str(pizzas) + "\n")

print()
print("As pizzas favoritas dos meus amigos são: " + str(friends_pizzas) + "\n")

print()
for pizza in pizzas:
    print("Minha Predileta é " + str(pizza))