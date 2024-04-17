# Creación de una lista utilizando un bucle for convencional.
numbers = []
# Itera sobre los números del 1 al 10.
for element in range(1, 11):
    # Multiplica cada número por 2 y lo agrega a la lista.
    numbers.append(element * 2)

# Imprime la lista resultante.
print(numbers)

# Creación de una lista utilizando una list comprehension.
numbers_v2 = [element * 2 for element in range(1, 11)]
# Imprime la lista resultante.
print(numbers_v2)

# Creación de una lista utilizando un bucle for convencional con una condición.
numbers = []
# Itera sobre los números del 1 al 10.
for i in range(1, 11):
    # Verifica si el número es par.
    if i % 2 == 0:
        # Multiplica el número por 2 y lo agrega a la lista.
        numbers.append(i * 2)

# Imprime la lista resultante.
print(numbers)

# Creación de una lista utilizando una list comprehension con una condición.
numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
# Imprime la lista resultante.
print(numbers_v2)
