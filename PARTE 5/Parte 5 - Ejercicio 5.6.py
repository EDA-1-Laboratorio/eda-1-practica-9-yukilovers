'''
Completa el código que agrupa una lista de tuplas (nombre, materia) en un diccionario 
donde la llave es la materia y el valor es la lista de alumnos:
'''

inscripciones = [
    ("Ana", "EDA"),
    ("Luis", "Cálculo"),
    ("María", "EDA"),
    ("Pedro", "Física"),
    ("Ana", "Cálculo"),
    ("Luis", "EDA"),
]

por_materia = {}
for nombre, materia in inscripciones:
    if materia not in por_materia:
        por_materia[materia] = []
    por_materia[materia].append(nombre)

for materia, alumnos in por_materia.items():
    print(f"  {materia}: {alumnos}")
