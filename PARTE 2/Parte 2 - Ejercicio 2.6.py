'''
Completa el código que verifica si una cadena es un palíndromo (se lee igual al derecho y al revés):
'''

def es_palindromo(texto):
    texto = texto.lower()        # Convertir a minúsculas
    texto = texto.replace(" ", "")  # Quitar espacios
    return texto == texto[::-1]      # Comparar con la cadena invertida

# Pruebas
print(es_palindromo("anilina"))      # True
print(es_palindromo("Reconocer"))    # True
print(es_palindromo("Python"))       # False
print(es_palindromo("Oso"))          # True
