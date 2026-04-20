'''
Escribe y ejecuta el siguiente código sobre operaciones avanzadas con diccionarios:
'''

# Método get() — evita errores si la llave no existe
alumno = {"nombre": "Juan", "edad": 20}

print(alumno.get("nombre"))         # Juan
print(alumno.get("telefono"))       # None (no lanza error)
print(alumno.get("telefono", "N/A")) # N/A (valor por defecto)

# En contraste, esto SÍ lanza error:
# print(alumno["telefono"])  → KeyError

# Eliminar un par llave:valor
del alumno["edad"]
print(alumno)  # {"nombre": "Juan"}

# Combinar dos diccionarios
datos1 = {"a": 1, "b": 2}
datos2 = {"b": 20, "c": 30}
datos1.update(datos2)
print(datos1)  # {"a": 1, "b": 20, "c": 30}  (b se sobreescribe)

# Diccionario a partir de listas con zip
llaves = ["nombre", "edad", "carrera"]
valores = ["Ana", 19, "Computación"]
diccionario = dict(zip(llaves, valores))
print(diccionario)

'''
Ejecución del código en python:
Juan
None
N/A
{'nombre': 'Juan'}
{'a': 1, 'b': 20, 'c': 30}
{'nombre': 'Ana', 'edad': 19, 'carrera': 'Computación'}
'''
