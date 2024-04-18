def get_population(country_dict):
    """
    Función para obtener la población de un país de un diccionario dado.

    Parámetros:
    country_dict (dict): Un diccionario que contiene datos de población de un país.

    Retorna:
    tuple: Una tupla que contiene las etiquetas y los valores de población.
    """
    # Crear un nuevo diccionario con las poblaciones de diferentes años como valores enteros
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }
    # Obtener las etiquetas (años) y los valores (poblaciones) del diccionario
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


def population_by_country(data, country):
    """
    Función para obtener datos de población de un país específico.

    Parámetros:
    data (list): Una lista de diccionarios que contiene datos de múltiples países.
    country (str): El nombre del país del cual se desea obtener datos de población.

    Retorna:
    list: Una lista de diccionarios que contiene datos de población del país especificado.
    """
    # Filtrar la lista de datos para obtener solo los datos del país especificado
    result = list(filter(lambda item: item['Country'] == country, data))
    return result
