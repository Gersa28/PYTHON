# Intenta ejecutar algunas operaciones y manejar los errores si ocurren

# Esta línea provocará un error de división por cero
# print(0 / 0)

# La siguiente línea generará un NameError porque 'result' no está definido
# print(result)

# Imprime 'Hola' antes de que ocurran los errores
print('Hola')

# Define una función de suma usando una expresión lambda
suma = lambda x,y: x + y

# Utiliza una aserción para verificar si la suma de 2 y 2 es igual a 4
assert suma(2,2) == 4

# Si la aserción falla, el programa se detiene aquí y no se imprime 'Hola 2'

# Si la aserción pasa, imprime 'Hola 2' después de la aserción
print('Hola 2')

# Define una variable 'age' con un valor de 10
age = 10

# Comprueba si 'age' es menor que 18
if age < 18:
    # Si 'age' es menor que 18, genera una excepción con un mensaje personalizado
    raise Exception('No se permiten menores de edad')

# Si la excepción no se genera, imprime 'Hola 2' después de la comprobación
print('Hola 2')
