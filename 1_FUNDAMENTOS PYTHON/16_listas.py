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

# 2024 -----------------------------------------------------------
to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))
mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento:", mix[-1])
string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Ultimo elemento:", string[-1])
print(mix[2:-2])
print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers = [1,2,100.01,90.45,3,4, 5]
print(numbers)
print("Mayor:",max(numbers))
print("Menor:",min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers
#print(numbers)