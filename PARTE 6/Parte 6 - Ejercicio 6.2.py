'''
Escribe y ejecuta el siguiente código sobre funciones con argumentos variables:
'''

# Función con número variable de argumentos (*args)
def sumar_todos(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(sumar_todos(1, 2, 3))         # 6
print(sumar_todos(10, 20, 30, 40))   # 100

# Función con argumentos nombrados (**kwargs)
def crear_perfil(**datos):
    for llave, valor in datos.items():
        print(f"  {llave}: {valor}")

print("Perfil:")
crear_perfil(nombre="Ana", edad=20, carrera="Computación")

'''
Ejecución del código en python:
6
100
Perfil:
  nombre: Ana
  edad: 20
  carrera: Computación

'''
