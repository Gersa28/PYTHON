# aprederemos sobre la estructura de los diccionarios, en python se definen por un par llave-valor:
my_dic = {'persona, niño'}
print(my_dic)
print(type(my_dic))

my_dic = {
  'persona': 'niño',
  'nombre': 'nicolas',
  'genero':'masculino',
  'edad': '12 años'#aca estamos definiendo los datos de diccionario
}
print(my_dic)
print(len(my_dic))#con len podemos saber cuántos elementos tenemos en el dic

#tambien puedo leer ese diccionario con los métodos 
print(my_dic['persona'])
print(my_dic['nombre'])
print(my_dic['genero'])
print(my_dic['edad'])

#tambien hay otra forma de hacer que es con el método get
print(my_dic.get('persona'))
print(my_dic.get('nombre'))
print(my_dic.get('genero'))
print(my_dic.get('edad'))
print(my_dic.get('juan jose'))
#la diferencia con get es que imprímelos datos que no hay nada definido(none)
#es recomendable siempre trabajar con get, porque si no existe el diccionario no dará un error solo pondrá None 

#tambien podemos verificar si una llave no existe ni (IN), que nos arrojara valores bulenos 
print('persona' in my_dic)
print('apellidos' in my_dic)
#en esta clase vimos los primeros acercamientos a los diccionarios
