# Definición de una función llamada 'increment'
def increment(x):   
    return x + 1

# Definición de una función lambda llamada 'increment_v2'
# que realiza la misma operación que la función 'increment'
increment_v2 = lambda x: x + 1

# Definición de una función de orden superior llamada 'high_ord_func'
# que toma un valor 'x' y una función 'func' como argumentos,
# y devuelve la suma de 'x' y el resultado de aplicar 'func' a 'x'.
def high_ord_func(x, func):
    """
    Aplica una función 'func' a un valor 'x' y devuelve la suma de 'x' y el resultado de la función.
    
    Args:
        x (int): El valor al que se aplicará la función.
        func (function): La función que se aplicará a 'x'.
    
    Returns:
        int: La suma de 'x' y el resultado de aplicar 'func' a 'x'.
    """
    return x + func(x)

# Definición de una función lambda de orden superior llamada 'high_ord_func_v2'
# que realiza la misma operación que la función 'high_ord_func' pero utilizando una función lambda.
high_ord_func_v2 = lambda x, func: x + func(x)

# Llamada a la función 'high_ord_func' con los argumentos 2 y 'increment'
# y el resultado se asigna a la variable 'result'
# El resultado es 2 + (2 + 1) = 5
result = high_ord_func(2, increment)
print(result)

# Llamada a la función 'high_ord_func_v2' con los argumentos 2 y 'increment_v2'
# y el resultado se asigna a la variable 'result'
# El resultado es 2 + (2 + 1) = 5
result = high_ord_func_v2(2, increment_v2)
print(result)

# Llamada a la función 'high_ord_func_v2' con los argumentos 2 y una función lambda que suma 2 a 'x'
# y el resultado se asigna a la variable 'result'
# El resultado es 2 + (2 + 2) = 6
result = high_ord_func_v2(2, lambda x: x + 2)
print(result)

# Llamada a la función 'high_ord_func_v2' con los argumentos 2 y una función lambda que multiplica 'x' por 5
# y el resultado se asigna a la variable 'result'
# El resultado es 2 + (2 * 5) = 12
result = high_ord_func_v2(2, lambda x: x * 5)
print(result)
