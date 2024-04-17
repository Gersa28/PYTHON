# Lista de diccionarios que representan diferentes productos y sus precios
items = [
    {'product': 'camisa', 'price': 100},
    {'product': 'pantalones', 'price': 300},
    {'product': 'pantalones 2', 'price': 200}
]

# Utilizar la función map junto con una función lambda para extraer los precios de cada elemento en la lista 'items'
prices = list(map(lambda item: item['price'], items))

# Imprimir la lista original de 'items' y la lista de precios extraídos
print("Lista original de items:", items)
print("Precios extraídos:", prices)

# Definir una función llamada 'add_taxes' que calcula los impuestos para un elemento dado
# y añade una nueva clave 'taxes' al diccionario del elemento con el valor de impuestos calculado
def add_taxes(item):
    item['taxes'] = item['price'] * 0.19
    return item

# Utilizar la función map para aplicar la función 'add_taxes' a cada elemento en la lista 'items'
# y crear una nueva lista 'new_items' con los impuestos añadidos a cada elemento
new_items = list(map(add_taxes, items))

# Imprimir la lista 'new_items' con los impuestos añadidos y la lista 'items' original
print("Nuevos items con impuestos añadidos:", new_items)
print("Lista original de items:", items)
