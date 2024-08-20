name = "Nicolas"
last_name = 'Molina Monroy'
print(name)
print(last_name)

#CONCATENACIÓN
full_name = name + " " + last_name
print(full_name)

quote = "I'm Nicolas"
print(quote)

quote2 = 'She said "Hello"  '
print(quote2)

# f de format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name} \n"
print('v3', template)

name = 'CARLA Marcela'
last_name = '   Florida     Roman  '
print(5 * name)
print(name + ' ' + last_name)
print(len(name))
print(len(last_name))
print(name.lower())
print(name.upper())
print(last_name.strip())