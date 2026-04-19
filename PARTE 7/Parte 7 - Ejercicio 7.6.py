'''
Completa la función que clasifica un carácter según su tipo:
'''
def clasificar_caracter(c):
    if c.isalpha():        # ¿Es una letra?
        if c.isupper():    # ¿Es mayúscula?
            return "Letra mayúscula"
        else:
            return "Letra minúscula"
    elif c.isdigit():      # ¿Es un dígito?
        return "Dígito"
    elif c == " ":
        return "Espacio"
    else:
        return "Carácter especial"

# Pruebas
print(clasificar_caracter("A"))   # Letra mayúscula
print(clasificar_caracter("z"))   # Letra minúscula
print(clasificar_caracter("5"))   # Dígito
print(clasificar_caracter(" "))   # Espacio
print(clasificar_caracter("@"))   # Carácter especial
