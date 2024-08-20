'''
for element in range(1, 21):
  print(element)

'''

my_list = [23, 45, 67, 89 ,43]
for element in my_list:
  print(element)

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
  print(element)


product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}

for key in product:
  print(key, '=>', product[key])

# Inicia un bucle for que itera sobre los elementos del diccionario 'product'.
# El método items() devuelve una vista de objetos tipo tuple, 
# donde cada tuple contiene una clave y su valor asociado del diccionario.
for key, value in product.items():  
    # Dentro del bucle, se imprime la clave (key) y su valor (value)
    # separados por la flecha '=>'.
    # En cada iteración, 'key' toma el valor de una de las claves del diccionario,
    # y 'value' toma el valor asociado a esa clave.
    print(key, '=>', value)


people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]

for person in people:
  print('name =>', person['name'])