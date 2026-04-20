
'''
Escribe y ejecuta el siguiente código que muestra el uso de condiciones con operadores lógicos y el operador in:
'''

# Verificar rango con comparación encadenada
temp = 25
if 20 <= temp <= 30:
    print("Temperatura agradable")

# Usar "in" para verificar pertenencia
dia = "sábado"
if dia in ("sábado", "domingo"):
    print(f"{dia} es fin de semana")
else:
    print(f"{dia} es día laboral")

# Condiciones múltiples con and/or
edad = 20
tiene_credencial = True
if edad >= 18 and tiene_credencial:
    print("Puede entrar")

# Verificar si una cadena está vacía
nombre = ""
if not nombre:
    print("El nombre está vacío")  # Las cadenas vacías son "falsy"

# Valores "truthy" y "falsy"
# Falsy: 0, 0.0, "", [], {}, (), None, False
# Truthy: todo lo demás
print(bool(0))      # False
print(bool(42))     # True
print(bool(""))     # False
print(bool("hola")) # True
print(bool([]))     # False
print(bool([1]))    # True

'''
Ejecución del código en python:
Temperatura agradable
sábado es fin de semana
Puede entrar
El nombre está vacío
False
True
False
True
False
True

'''
