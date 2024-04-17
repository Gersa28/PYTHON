# Definición de una función llamada 'increment'
def increment(x):
    """
    Incrementa el valor de x en 1 y devuelve el resultado.
    
    Args:
        x (int): El valor que se incrementará en 1.
    
    Returns:
        int: El resultado de incrementar x en 1.
    """
    return x + 1

# Definición de una función lambda llamada 'increment_v2'
# que realiza la misma operación que la función 'increment'
increment_v2 = lambda x: x + 1

# Llamada a la función 'increment' con el argumento 10
# y el resultado se asigna a la variable 'result'
result = increment(10)
print(result)  # Imprime 11

# Llamada a la función lambda 'increment_v2' con el argumento 20
# y el resultado se asigna a la variable 'result'
result = increment_v2(20)
print(result)  # Imprime 21

# Definición de una función lambda llamada 'full_name'
# que recibe dos argumentos 'name' y 'last_name'
# y devuelve una cadena formateada con el nombre completo.
full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

# Llamada a la función lambda 'full_name' con los argumentos 'nicolas' y 'perez casas'
# y el resultado se asigna a la variable 'text'
text = full_name('nicolas', 'perez casas')
print(text)  # Imprime 'Full name is Nicolas Perez Casas'
