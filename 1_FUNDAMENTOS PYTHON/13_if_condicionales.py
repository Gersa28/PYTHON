if True:
  print('debería ejecutarse')

if False:
  print('nunca se ejecuta')

number = int(input('Ingrese un número => '))
result = number % 2 #Nos devuelve el resto de la división de number sobre 2
if (result == 0):
	print('Es par')
else:
	print('Es impar')

pet = input('¿Cuál es tu mascota favorita? ')

if pet == 'perro':
  print('genial tienes buen gusto')
elif pet == 'gato':
  print('espero tengas suerte')
elif pet == 'pez':
  print('eres lo máximo')
else:
  print('no tienes ninguna mascota interesante')
