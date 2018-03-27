my_foods = ['pizza', 'falafel', 'carrot cake', 'spaguetti', 'file', 'potatos']
friends_foods = my_foods[:]
my_foods.append('cannoli')
friends_foods.append('ice_cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend´s favorite foods are:")
print(friends_foods)

print()
print("Os três primeiros itens da lista são:\n " + str(my_foods[:3]))

print()
print("Três itens do meio da lista são: " + str(my_foods[2:4]))

print()
print("Os três últimos itens da lista são: " + str(my_foods[3:]))
