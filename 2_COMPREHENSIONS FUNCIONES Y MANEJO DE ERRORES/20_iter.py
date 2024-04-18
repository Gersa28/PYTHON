# Iteración a través de un rango del 1 al 9 (inclusive)
for i in range(1, 10):
    print(i)
    # Imprime los números del 1 al 9 en cada iteración del bucle

# Creación de un iterador a partir de un rango del 1 al 3 (inclusive)
my_iter = iter(range(1, 4))
# Iterador creado a partir de un rango del 1 al 3

print(my_iter)  # Imprime el objeto iterador creado
print(next(my_iter))  # Imprime el próximo elemento del iterador (1)
print(next(my_iter))  # Imprime el próximo elemento del iterador (2)
print(next(my_iter))  # Imprime el próximo elemento del iterador (3)
print(next(my_iter))  # Genera una excepción StopIteration ya que el iterador está agotado
