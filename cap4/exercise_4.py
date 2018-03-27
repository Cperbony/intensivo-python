for value in range (1, 20):
    print(value)

one_million = list(range(1, 10000))
print(one_million)
print(min(one_million))
print(max(one_million))
print(sum(one_million))

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

multiple_of_threes = list(range(3, 31, 3))

print()
print("List of multiples of 3")
for number in multiple_of_threes:
    print(number)

print()
print("List of Cubes")
cubes = list(range(1, 11))
for cube in cubes:
    cube = cube**3
    print(cube)

print()
print("Cube Comprehension")
cubes = [value**3 for value in range(1, 11)]

for cube in cubes:
    print(cube)
