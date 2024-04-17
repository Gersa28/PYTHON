# Definir una lista de números
numbers = [1, 2, 3, 4]

# Utilizar un bucle for para duplicar cada elemento de la lista 'numbers'
doubled_numbers_for_loop = []
for i in numbers:
    doubled_numbers_for_loop.append(i * 2)

# Utilizar la función map junto con una función lambda para duplicar cada elemento de la lista 'numbers'
doubled_numbers_map_lambda = list(map(lambda i: i * 2, numbers))

# Imprimir las listas originales y las nuevas listas creadas
print("Lista original de números:", numbers)
print("Números duplicados (con bucle for):", doubled_numbers_for_loop)
print("Números duplicados (con map y lambda):", doubled_numbers_map_lambda)

# Definir dos listas de números
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

# Imprimir las dos listas originales
print("Números 1:", numbers_1)
print("Números 2:", numbers_2)

# Utilizar la función map junto con una función lambda para sumar elemento por elemento
# de las dos listas 'numbers_1' y 'numbers_2'
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))

# Imprimir el resultado de la suma de las dos listas
print("Resultado de la suma de elementos:", result)

# Ejemplo Ilustrativo
ingredientes = ['🐏' , '🐓','🐟','🐖']
preparacion = ['🍔','🍗','🍣','🥓']
print(ingredientes)
print(preparacion)
result=list(map(lambda a,b:'Con '+ a +' se puede hacer '+ b, ingredientes,preparacion)) # Usando MAP
print(result)
