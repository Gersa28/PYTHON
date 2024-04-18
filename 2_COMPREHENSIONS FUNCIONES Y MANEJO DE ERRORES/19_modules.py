import sys
# sys proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete.
print(sys.path)  # Imprime los directorios donde Python busca los módulos al importar

import re
# re es un módulo que proporciona operaciones de coincidencia de patrones similares a las que se encuentran en Perl.
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)  # Encuentra todos los números en el texto utilizando una expresión regular
print(result)  # Imprime la lista de números encontrados

import time
# time proporciona funciones para trabajar con el tiempo, incluyendo la conversión entre representaciones de tiempo, obtención de la hora actual y medición del tiempo de ejecución de un programa.
timestamp = time.time()  # Obtiene el tiempo actual en segundos desde la época
print(timestamp)  # Imprime el timestamp

local = time.localtime()  # Obtiene la hora local actual como una estructura de tiempo
result = time.asctime(local)  # Convierte la estructura de tiempo en una cadena de tiempo legible
print(result)  # Imprime la hora local actual

import collections
# collections proporciona contenedores especializados y de alto rendimiento que son alternativas a los contenedores generales de Python.
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)  # Crea un objeto Counter que cuenta la frecuencia de cada elemento en la lista
print(counter)  # Imprime el objeto Counter
