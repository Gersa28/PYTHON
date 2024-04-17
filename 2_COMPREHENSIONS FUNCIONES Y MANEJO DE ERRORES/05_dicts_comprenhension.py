# Creación de un diccionario utilizando un bucle for convencional.
dict = {}
# Itera sobre los números del 1 al 4.
for i in range(1, 5):
    # Asigna a cada número su doble como valor en el diccionario.
    dict[i] = i * 2

# Imprime el diccionario resultante.
print(dict)

# Creación de un diccionario utilizando dictionary comprehension.
dict_v2 = {i: i * 2 for i in range(1, 5)}
# Imprime el diccionario resultante.
print(dict_v2)

# Creación de un diccionario de población utilizando un bucle for convencional con valores aleatorios.
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
# Itera sobre cada país en la lista de países.
for country in countries:
    # Asigna a cada país un valor aleatorio de población entre 1 y 100.
    population[country] = random.randint(1, 100)

# Imprime el diccionario de población resultante.
print(population)

# Creación de un diccionario de población utilizando dictionary comprehension con valores aleatorios.
population_v2 = {country: random.randint(1, 100) for country in countries}
# Imprime el diccionario de población resultante.
print(population_v2)

# Creación de una lista de tuplas combinando nombres y edades utilizando la función zip().
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
# Combina los nombres y edades en una lista de tuplas.
print(list(zip(names, ages)))

# Creación de un diccionario utilizando dictionary comprehension con nombres como claves y edades como valores.
new_dict = {name: age for (name, age) in zip(names, ages)}
# Imprime el diccionario resultante.
print(new_dict)
