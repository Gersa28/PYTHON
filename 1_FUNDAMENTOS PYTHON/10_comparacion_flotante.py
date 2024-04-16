x = 3.3
print(x)
print("Imprimiré y:")
y = 1.1 + 2.2 # Esto no será igual a x
print(y) # Ver cantidad de Decimales
print(x == y) # False

y_str = format(y, ".2g")
print('str =>', y_str)
print(y_str == str(x))

print('*' * 10)

print(y, x)

tolerance = 0.00001
print(abs(x - y) < tolerance)
