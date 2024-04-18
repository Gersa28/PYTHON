try:
    # Intenta ejecutar algunas operaciones que pueden generar errores

    # Esta línea provocará un error de división por cero
    print(0 / 0)

    # Esta línea provocará un AssertionError porque 1 es igual a 1
    assert 1 != 1, 'Uno no es igual que uno'

    # Define una variable 'age' con un valor de 10
    age = 10

    # Comprueba si 'age' es menor que 18
    if age < 18:
        # Si 'age' es menor que 18, genera una excepción con un mensaje personalizado
        raise Exception('No se permiten menores de edad')

# Captura los errores específicos y maneja cada uno de ellos
except ZeroDivisionError as error:
    # Si ocurre un error de división por cero, imprime el mensaje de error específico
    print(error)
except AssertionError as error:
    # Si ocurre un error de aserción, imprime el mensaje de error específico
    print(error)
except Exception as error:
    # Si ocurre cualquier otro tipo de error, imprime el mensaje de error genérico
    print(error)

# Después de manejar los errores o si no se producen errores, continúa con la ejecución normal
print('Hola')
print('Hola 2')
