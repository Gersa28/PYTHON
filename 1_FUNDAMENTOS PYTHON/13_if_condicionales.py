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
