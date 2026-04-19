'''
Completa la función que cuenta cuántas vocales y consonantes tiene una cadena:
'''
def contar_vocales_consonantes(texto):
    vocales = "aeiouáéíóú"
    texto = texto.lower()  # Convertir a minúsculas
    num_vocales = 0
    num_consonantes = 0
    for c in texto:
        if c.isalpha():    # Solo letras (ignora espacios, números, etc.)
            if c in vocales:
                num_vocales += 1
            else:
                num_consonantes += 1
    return num_vocales, num_consonantes

# Pruebas
v, c = contar_vocales_consonantes("Hola Mundo")
print(f"Vocales: {v}, Consonantes: {c}")  # Vocales: 4, Consonantes: 5

v, c = contar_vocales_consonantes("Python")
print(f"Vocales: {v}, Consonantes: {c}")  # Vocales: 1, Consonantes: 5
