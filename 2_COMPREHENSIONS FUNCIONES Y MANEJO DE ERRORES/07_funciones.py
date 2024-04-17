# Imprime 'Hola' en la consola
print('Hola')

# Definición de una función que imprime el texto proporcionado dos veces
def my_print(text):
    """
    Imprime el texto proporcionado dos veces.

    Parámetros:
        text (str): El texto que se imprimirá dos veces.
    """
    print(text * 2)

# Llamadas a la función my_print con diferentes argumentos
my_print('Este es mi texto')  # Imprime 'Este es mi textoEste es mi texto'
my_print('Hola')               # Imprime 'HolaHola'

# Definición de variables a, b y c, y su suma
a = 10
b = 90
c = a + b

# Definición de una función que imprime la suma de dos números utilizando la función my_print
def suma(a, b):
    """
    Ejemplo de Documentación:
    Imprime la suma de dos números utilizando la función my_print.

    Parámetros:
        a (int): El primer número.
        b (int): El segundo número.
    """
    my_print(a + b)

# Llamadas a la función suma con diferentes argumentos y sus resultados esperados
suma(1, 5)   # Imprime '6'
suma(10, 4)  # Imprime '14'
