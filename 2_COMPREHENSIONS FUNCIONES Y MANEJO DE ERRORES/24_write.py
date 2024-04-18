# Abre el archivo 'texs.txt' en modo de escritura y lectura ('w+')
# Si el archivo no existe, se crea; si existe, se trunca
with open('./texs.txt', 'w+') as file:

    # Itera sobre cada línea del archivo (en este caso, como se abre en modo de escritura, no hay líneas aún)
    # Por lo tanto, este bucle no realiza ninguna iteración
    for line in file:
        print(line)

    # Escribe una cadena en el archivo, seguida de un salto de línea
    file.write('nuevas cosas en este archivo\n')

    # Escribe otra cadena en el archivo, seguida de un salto de línea
    file.write('otra linea\n')

    # Escribe una tercera cadena en el archivo, seguida de un salto de línea
    file.write('mas linea\n')
