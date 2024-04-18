import csv  # Importamos el módulo csv para leer archivos CSV

def read_csv(path):
    """
    Función para leer datos de un archivo CSV y convertirlos en una lista de diccionarios.

    Parámetros:
    path (str): La ruta del archivo CSV.

    Retorna:
    list: Una lista de diccionarios que contiene los datos del archivo CSV.
    """
    with open(path, 'r') as csvfile:  # Abrir el archivo CSV en modo lectura
        reader = csv.reader(csvfile, delimiter=',')  # Crear un objeto lector de CSV
        header = next(reader)  # Leer la fila de encabezado del archivo CSV
        data = []  # Inicializar una lista vacía para almacenar diccionarios
        for row in reader:  # Iterar sobre cada fila en el archivo CSV
            iterable = zip(header, row)  # Asociar cada encabezado con su valor de fila correspondiente
            country_dict = {key: value for key, value in iterable}  # Crear un diccionario para la fila
            data.append(country_dict)  # Agregar el diccionario a la lista de datos
    return data  # Devolver la lista de diccionarios que contiene los datos del archivo CSV

if __name__ == '__main__':
    # Si el script se ejecuta directamente, leer el archivo CSV e imprimir la primera fila de datos
    data = read_csv('./data.csv')
    print(data[0])  # Imprimir la primera fila de datos
