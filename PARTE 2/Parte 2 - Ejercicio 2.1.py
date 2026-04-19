'''
Ejercicio 2.1 — Replica el ejemplo
Crea un archivo cadenas.py con el siguiente código. Ejecútalo y verifica la salida.
'''

nombre = "Ada"
apellido = "Lovelace"

# Concatenación con +
print(nombre + " " + apellido)

# Concatenación con format
print("Nombre: {}, Apellido: {}".format(nombre, apellido))

# Cambiar orden con format
print("Apellido: {1}, Nombre: {0}".format(nombre, apellido))

# f-string
print(f"Programadora: {nombre} {apellido}")

# Caracteres de escape
print("Línea 1\nLínea 2")
print("Columna1\tColumna2")

# SALIDA
'''
Ada Lovelace
Nombre: Ada, Apellido: Lovelace
Apellido: Lovelace, Nombre: Ada
Programadora: Ada Lovelace
Línea 1
Línea 2
Columna1        Columna
'''
