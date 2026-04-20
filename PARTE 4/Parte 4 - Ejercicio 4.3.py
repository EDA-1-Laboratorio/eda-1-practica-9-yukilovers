# Crear una lista con los cuadrados del 1 al 10
# Forma clásica (como en C):
cuadrados = []
for i in range(1, 11):
    cuadrados.append(i ** 2)
print("Clásica:", cuadrados)

# Forma con list comprehension (exclusiva de Python):
cuadrados = [i ** 2 for i in range(1, 11)]
print("Comprehension:", cuadrados)

# Filtrar: solo los pares
pares = [x for x in range(1, 21) if x % 2 == 0]
print("Pares:", pares)

# Transformar: longitud de cada palabra
palabras = ["hola", "mundo", "python", "es", "genial"]
longitudes = [len(p) for p in palabras]
print("Longitudes:", longitudes)  # [4, 5, 6, 2, 6]
