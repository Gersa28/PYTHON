# Ejemplo de iterador

#Crear una lista
my_list = [1,2,3,4]

#Obtener el iterador
my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))

# Crear un iterador para los numeros impares

#Limite
limit = 10
#Crear iterador
odd_itter = iter(range(1,limit+1,2))
#Usar el iterador
for num in odd_itter:
    print(num)

# Iterar en cadenas
#Creando la cadena
text = "Hola mundo"
#Creando el iterador
iter_text = iter(text)

#Iterar en la cadena
for char in iter_text:
    print(char)


# Ejemplo de Generador
def mi_generador():
    yield 1
    yield 2
    yield 3

# Usar el generador
for valor in mi_generador():
    print(valor)