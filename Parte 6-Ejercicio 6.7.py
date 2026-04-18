'''
Completa la función que recibe una lista de diccionarios y retorna el que tenga el mayor 
valor en una llave dada:

'''

def encontrar_maximo(lista, llave):
    if not lista:
        return None
    maximo = lista[0]
    for elemento in lista:
        if elemento[llave] > maximo[llave]:
            maximo = elemento
    return maximo

# Pruebas
productos = [
    {"nombre": "Laptop", "precio": 15000},
    {"nombre": "Teclado", "precio": 500},
    {"nombre": "Monitor", "precio": 8000},
    {"nombre": "Mouse", "precio": 300},
]

caro = encontrar_maximo(productos, "precio")
print(f"Más caro: {caro['nombre']} (${caro['precio']})")
# Más caro: Laptop ($15000)
