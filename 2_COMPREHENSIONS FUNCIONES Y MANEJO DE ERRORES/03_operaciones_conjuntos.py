# Definición de dos conjuntos, set_a y set_b, con elementos únicos.
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Unión de los conjuntos set_a y set_b para obtener un nuevo conjunto que contenga todos los elementos de ambos conjuntos sin duplicados.
set_c = set_a.union(set_b)
# Imprime el resultado de la unión.
print(set_c)
# También se puede realizar la unión utilizando el operador | (pipe).
print(set_a | set_b)

# Intersección de los conjuntos set_a y set_b para obtener un nuevo conjunto que contenga solo los elementos que están presentes en ambos conjuntos.
set_c = set_a.intersection(set_b)
# Imprime el resultado de la intersección.
print(set_c)
# También se puede realizar la intersección utilizando el operador & (ampersand).
print(set_a & set_b)

# Diferencia entre los conjuntos set_a y set_b para obtener un nuevo conjunto que contenga los elementos que están en set_a pero no en set_b.
set_c = set_a.difference(set_b)
# Imprime el resultado de la diferencia.
print(set_c)
# También se puede calcular la diferencia utilizando el operador - (guión).
print(set_a - set_b)

# Diferencia simétrica entre los conjuntos set_a y set_b para obtener un nuevo conjunto que contenga los elementos que están en uno de los conjuntos pero no en ambos.
set_c = set_a.symmetric_difference(set_b)
# Imprime el resultado de la diferencia simétrica.
print(set_c)
# También se puede calcular la diferencia simétrica utilizando el operador ^ (circunflejo).
print(set_a ^ set_b)
