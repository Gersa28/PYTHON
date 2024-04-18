import functools  # Importa el módulo functools para usar la función reduce

numbers = [1, 2, 3, 4]  # Lista de números

def accum(counter, item):
    """
    Función que se pasa como argumento a reduce.
    Toma dos argumentos, `counter` y `item`, y devuelve la suma de ambos.
    """
    print('counter => ', counter)  # Imprime el valor actual del contador
    print('item => ', item)  # Imprime el valor actual del ítem
    return counter + item  # Devuelve la suma de `counter` y `item`

result = functools.reduce(accum, numbers)  # Utiliza functools.reduce para aplicar la función accum a la lista de números

print(result)  # Imprime el resultado de la reducción
"""
La función reduce aplicada aquí toma dos argumentos: una función acumuladora (accum) y una secuencia (numbers).
Reduce aplica la función acumuladora de manera iterativa sobre la secuencia, tomando dos elementos a la vez: 
el valor acumulado (counter) y el siguiente elemento de la secuencia (item). 
El valor acumulado se actualiza en cada iteración de acuerdo con la lógica definida en la función accum. 
Finalmente, reduce devuelve el valor acumulado después de procesar toda la secuencia. 
En este caso, devuelve la suma de todos los elementos de la lista numbers.
"""
