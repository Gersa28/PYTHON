
import random

def busqueda_binaria(arreglo, objetivo):
  arreglo =  sorted(arreglo)
  minimo = 0
  maximo = len(arreglo)

  while minimo < maximo:
    # Revisa el elemento en la mitad de min y max
    mitad = (maximo + minimo) // 2
    val = arreglo[mitad]

    if val == objetivo:
      # Encontramos el objetivo
      print("Número encontrado en la posición")
      return mitad
    elif objetivo < val:
      # En este caso, buscamos los elementos
      # a la izquierda del objetivo
      maximo = mitad
    elif objetivo > val:
      # Esta línea es para evitar un bucle infinito
      if minimo == mitad:
        break
      # El objetivo es más que el valor de la mitad,
      # entonces seguimos buscando con los elementos
      # a la derecha
      minimo = mitad

  # No encontramos el objetivo
  return "Número no Encontrado"

# Genera una lista de 20 números aleatorios únicos entre 1 y 100
arreglo = random.sample(range(1, 200), 50)
arreglo_ordenado=sorted(arreglo)
print(arreglo_ordenado)
print(busqueda_binaria(arreglo, 20))