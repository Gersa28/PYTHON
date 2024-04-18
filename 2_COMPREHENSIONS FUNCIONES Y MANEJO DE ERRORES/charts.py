import matplotlib.pyplot as plt
# Importa la biblioteca matplotlib.pyplot, que proporciona funciones para crear gráficos y visualizaciones.

def generate_bar_chart(labels, values):
    """
    Genera un gráfico de barras a partir de las etiquetas y los valores dados.

    Parámetros:
    - labels: Una lista de etiquetas para las barras.
    - values: Una lista de valores para las barras.
    """
    fig, ax = plt.subplots()  # Crea una figura y un conjunto de ejes.
    ax.bar(labels, values)  # Crea un gráfico de barras con las etiquetas y los valores dados.
    plt.show()  # Muestra el gráfico.

def generate_pie_chart(labels, values):
    """
    Genera un gráfico circular (de pastel) a partir de las etiquetas y los valores dados.

    Parámetros:
    - labels: Una lista de etiquetas para las porciones del gráfico circular.
    - values: Una lista de valores para las porciones del gráfico circular.
    """
    fig, ax = plt.subplots()  # Crea una figura y un conjunto de ejes.
    ax.pie(values, labels=labels)  # Crea un gráfico circular con las etiquetas y los valores dados.
    ax.axis('equal')  # Configura los ejes para que el gráfico sea circular.
    plt.show()  # Muestra el gráfico.

if __name__ == '__main__':
    labels = ['a', 'b', 'c']  # Etiquetas de ejemplo para los datos del gráfico.
    values = [10, 40, 800]  # Valores de ejemplo para los datos del gráfico.

    # Llamada a la función para generar un gráfico de barras.
    # generate_bar_chart(labels, values)

    # Llamada a la función para generar un gráfico circular (de pastel).
    generate_pie_chart(labels, values)