import random

# Lista de países
countries = ['col', 'mex', 'bol', 'pe']

# Generar un diccionario de población aleatoria para cada país
population_v2 = {country: random.randint(1, 100) for country in countries}
print("Diccionario de población por país:", population_v2)

# Filtrar países con población mayor a 50
result = {country: population for (country, population) in population_v2.items() if population > 50}
print("Países con población mayor a 50:", result)

# Crear un diccionario de vocales únicas en mayúsculas
text = 'Hola, soy Nicolas'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print("Diccionario de vocales únicas en mayúsculas:", unique)
