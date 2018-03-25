invited_persons_list = ['Lucas', 'Nathila', 'Lucia', 'Alzira']

name = invited_persons_list[0].title()
print(name + " Você esta convidado para o jantar")

name = invited_persons_list[1].title()
print(name + " Você esta convidado para o jantar")

name = invited_persons_list[2].title()
print(name + "Você está convidado para o jantar")

print("O convidado " + invited_persons_list[1] + " Não poderá comparecer ao Jantar")

invited_persons_list[1] = 'Matheus'
print("O novo convidade é o " + invited_persons_list[1])

invited_persons_list.append('José')
invited_persons_list.append('João')
invited_persons_list.append('Marcos')
print(invited_persons_list)

invited_persons_list.insert(0, 'Paulo')
invited_persons_list.insert(7, 'Davi')
invited_persons_list.insert(5, 'Salomão')
print(invited_persons_list)

invited_persons_list.pop();
print(invited_persons_list)

invited_persons_list.pop()
print(invited_persons_list)

invited_persons_list.pop()
print(invited_persons_list)

invited_persons_list.pop()
print(invited_persons_list)

invited_persons_list.pop()
print(invited_persons_list)

invited_persons_list.pop()
print(invited_persons_list)

invited_persons_list.pop()
print(invited_persons_list)

invited_persons_list.pop()
print(invited_persons_list)

to_be_removed = invited_persons_list[0]
invited_persons_list.remove(to_be_removed)
print(invited_persons_list)





