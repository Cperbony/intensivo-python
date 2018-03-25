cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Lista de Carros sem o sort " + str(cars))
cars2 = cars

cars.sort()
print("Lista de Carros com o sort " + str(cars))

cars.sort(reverse=True)
print("Lista de Carros com o sort REVERSE True " + str(cars))

cars.sort(reverse=False)
print("Lista de Carros com o sort REVERSE False " + str(cars))

cars = cars2
print("Lista de Carros com a cópia do primeiro cars" + str(cars))
print("Não retorna à lista original" + str(cars))

cars.reverse()
print("Inverte a ordem da lista" + str(len(cars)))