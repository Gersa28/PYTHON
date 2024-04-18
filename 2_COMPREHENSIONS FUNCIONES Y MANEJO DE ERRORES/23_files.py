# Abre el archivo 'text.txt' en modo de lectura y asigna el objeto de archivo a la variable 'file'
file = open('./text.txt')

# Lee todo el contenido del archivo y lo imprime (comentado para evitar impresiones innecesarias)
# print(file.read())

# Lee la primera línea del archivo y la imprime (comentado)
# print(file.readline())

# Lee la segunda línea del archivo y la imprime (comentado)
# print(file.readline())

# Lee la tercera línea del archivo y la imprime (comentado)
# print(file.readline())

# Lee la cuarta línea del archivo y la imprime (comentado)
# print(file.readline())

# Itera sobre cada línea del archivo e imprime cada línea
for line in file:
    print(line)

# Cierra el archivo después de que el bucle haya terminado de iterar
file.close()

# Abre el archivo 'text.txt' en un contexto 'with' que se encarga automáticamente de cerrar el archivo al salir del bloque
with open('./text.txt') as file:
    # Itera sobre cada línea del archivo e imprime cada línea
    for line in file:
        print(line)
