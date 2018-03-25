motorcycles = ['honda', 'yamaha', 'suzuki', 'bmw']
print(motorcycles)

motorcycles[0] = 'ducatti'
print(motorcycles)

motorcycles.append('suzuki special')
print(motorcycles)

motorcycles.insert(0, 'Honda2')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print('The first motorcycle i owned was a ' + first_owned.title() + '.')

print(motorcycles)

motorcycles[0] = last_owned
print(motorcycles)

motorcycles = ['honda3', 'ducatti', 'Yamaha2']
print(motorcycles)

too_expensive = 'ducatti'
motorcycles.remove(too_expensive)
print(motorcycles)


