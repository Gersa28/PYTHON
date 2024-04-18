import utils
# Importa el módulo utils que contiene funciones de utilidad para el proyecto.
import read_csv
# Importa el módulo read_csv que contiene funciones para leer datos de archivos CSV.
import charts
# Importa el módulo charts que contiene funciones para generar gráficos.

def run():
    """
    Función principal que ejecuta la lógica del programa.
    """
    # Lee los datos del archivo CSV './app/data.csv'.
    data = read_csv.read_csv('./data.csv')
    
    # Filtra los datos para obtener solo los países de Sudamérica.
    data = list(filter(lambda item : item['Continent'] == 'South America',data))

    # Extrae los nombres de los países y los porcentajes de población mundial.
    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    
    # Genera un gráfico circular (de pastel) con los países y porcentajes.
    charts.generate_pie_chart(countries, percentages)

    # Este bloque de código está comentado y no se ejecuta actualmente.
    '''
    # Solicita al usuario que ingrese un país.
    country = input('Type Country => ')
    
    # Busca el país ingresado en los datos.
    result = utils.population_by_country(data, country)

    # Si se encontró el país en los datos, genera un gráfico de barras con su población.
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)
    '''

if __name__ == '__main__':
    # Si este script se ejecuta directamente, llama a la función run().
    run()
