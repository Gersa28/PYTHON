numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
print(numbers)

# Definimos una función de filtrado para encontrar números impares
def es_impar(numero):
    return numero % 2 != 0

# Creamos una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtramos los números impares de la lista utilizando la función filter()
numeros_impares = filter(es_impar, numeros)

# Convertimos el resultado en una lista para visualización
numeros_impares_lista = list(numeros_impares)

# Imprimimos los números impares filtrados
print(numeros_impares_lista)  # Output: [1, 3, 5, 7, 9]

# Con lambda
numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
print(numbers)
