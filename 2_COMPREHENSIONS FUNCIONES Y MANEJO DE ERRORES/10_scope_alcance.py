# Definición de una variable global
price = 100  # Esta es una variable global, accesible desde cualquier parte del código

# Definición de una función llamada 'increment'
def increment():
    # Dentro de la función 'increment', se define una nueva variable 'price'
    # Esta es una variable local, distinta de la variable global 'price'
    price = 200  
    
    # Se define una nueva variable 'result' que es local a la función 'increment'
    result = price + 10  # 'price' aquí se refiere a la variable local de la función 'increment'
    print(result)  # Se imprime el resultado
    
    # Se devuelve el valor de 'result' como resultado de la función
    return result

# Se imprime el valor de la variable global 'price'
print(price)  # Esto imprimirá 100, ya que se refiere a la variable global definida al principio

# Se llama a la función 'increment' y se asigna su resultado a la variable 'price_2'
price_2 = increment()

# Se imprime el valor de 'price_2', que es el valor devuelto por la función 'increment'
print(price_2)

# Como se observa, la variable 'result' es local a la función 'increment' y no está disponible fuera de ella.
# Si se descomenta la línea siguiente, se generará un error, ya que 'result' no está definido en este ámbito.
# print(result)
