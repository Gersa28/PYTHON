def find_volume(length=1, width=1, depth=1):
    """
    Calcula el volumen de un objeto rectangular.

    Parámetros:
        length (float): La longitud del objeto (por defecto 1).
        width (float): El ancho del objeto (por defecto 1).
        depth (float): La profundidad del objeto (por defecto 1).

    Retorna:
        tuple: Una tupla que contiene el volumen calculado, el ancho proporcionado y una cadena de texto 'hola'.
    """
    return length * width * depth, width, 'hola'

# Llamada a la función find_volume con el argumento width=10 y asignación de los valores de retorno a las variables result, width y text
result, width, text = find_volume(width=10)

# Imprime el resultado del cálculo del volumen
print(result)

# Imprime el ancho proporcionado como argumento a la función
print(width)

# Imprime el texto 'hola'
print(text)

"""
El concepto de "retorno múltiple" en Python se refiere a la capacidad de una función para devolver más de un valor simultáneamente.
En el ejemplo dado, la función find_volume() retorna tres valores: el volumen calculado (length * width * depth),
el ancho proporcionado (width), y la cadena de texto 'hola'. Estos valores son empaquetados en una tupla y 
pueden ser desempaquetados en variables individuales cuando se llama a la función, como se muestra en la asignación result,
width, text = find_volume(width=10). Esto permite que la función retorne múltiples result
"""
