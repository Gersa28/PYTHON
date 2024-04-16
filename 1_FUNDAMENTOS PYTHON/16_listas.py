# Las Tuplas son inmutables, mientras que las Listas son mutables. 
# Las tuplas en Python son inmutables, lo que significa que una vez creada una tupla, 
# sus elementos no pueden cambiar. 
# Las tuplas no pueden ser alteradas, las Listas sí.
numbers_tupla = (1, 2, 3, 4) #TUPLA

numbers = [1, 2, 3, 4] #LISTA
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])
text = 'Hola'
# text[0] = 'W'

tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3])
print(True in types)
print('hola' in types)
