# Definición de un conjunto con elementos repetidos. Recordemos que no se admiten elementos suplicados.
set_countries = {"col", "mex", "bol", "col"}
# Imprime el conjunto.
print(set_countries)
# Imprime el tipo de dato del conjunto.
print(type(set_countries))

# Definición de un conjunto con números.
set_numbers = {1, 2, 3, 443, 23}
# Imprime el conjunto.
print(set_numbers)

# Definición de un conjunto con distintos tipos de datos.
set_types = {1, "hola", False, 12.12}
# Imprime el conjunto.
print(set_types)

# Creación de un conjunto a partir de una cadena de caracteres.
set_from_string = set("hola")
# Imprime el conjunto.
print(set_from_string)

# Creación de un conjunto a partir de una cadena de caracteres.
set_from_string = set("hoola")
# Imprime el conjunto.
print(set_from_string)

# Creación de un conjunto a partir de una tupla.
set_from_tuples = set(("abc", "cbv", "as", "abc"))
# Imprime el conjunto.
print(set_from_tuples)

# Definición de una lista con elementos repetidos.
numbers = [1, 2, 3, 1, 2, 3, 4]
# Convertir la lista a un conjunto para obtener elementos únicos.
set_numbers = set(numbers)
# Imprime el conjunto.
print(set_numbers)
# Convertir el conjunto nuevamente a una lista para obtener los elementos únicos en forma de lista.
unique_numbers = list(set_numbers)
# Imprime la lista con elementos únicos.
print(unique_numbers)
