'''
Escribe y ejecuta el siguiente código sobre tuplas con nombre (namedtuple):
'''
from collections import namedtuple

# Definir una tupla con nombre (similar a un struct de C)
Punto = namedtuple("Punto", ["x", "y"])
Alumno = namedtuple("Alumno", ["nombre", "carrera", "semestre"])

# Crear instancias
p = Punto(3, 7)
a = Alumno("Carlos", "Computación", 2)

# Acceso por nombre (como en un struct)
print(f"Punto: ({p.x}, {p.y})")
print(f"Alumno: {a.nombre}, {a.carrera}, semestre {a.semestre}")

# También se puede acceder por índice
print(f"Coordenada x: {p[0]}")

# Son inmutables (como las tuplas normales)
# p.x = 10  → AttributeError

'''
Ejecución del código en python:

Punto: (3, 7)
Alumno: Carlos, Computación, semestre 2
Coordenada x: 3
'''
