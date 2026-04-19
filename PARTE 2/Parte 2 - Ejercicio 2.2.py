'''
Ejercicio 2.2 — Replica el ejemplo
Escribe y ejecuta el siguiente código sobre operaciones con cadenas:
'''

mensaje = "  Estructura de Datos y Algoritmos  "

# Quitar espacios al inicio y final
print(mensaje.strip())

# Dividir una cadena en una lista (como strtok en C)
csv = "manzana,naranja,plátano,uva"
frutas = csv.split(",")
print(frutas)           # ['manzana', 'naranja', 'plátano', 'uva']

# Unir una lista en una cadena (operación inversa)
unida = " - ".join(frutas)
print(unida)            # manzana - naranja - plátano - uva

# Verificar contenido
print("datos" in mensaje)     # False
print(mensaje.startswith(" ")) # True

# Contar ocurrencias
texto = "abracadabra"
print(texto.count("a"))  # 5

# Encontrar posición (como strchr en C)
print(texto.find("cad"))  # 4 (índice donde empieza)
print(texto.find("xyz"))  # -1 (no encontrado)

'''
La salida es la siguiente: 

Estructura de Datos y Algoritmos
['manzana', 'naranja', 'plátano', 'uva']
manzana - naranja - plátano - uva
False
True
5
4
-1
'''
