'''
Ejercicio 10.5 — Completa el código
Completa el programa que genera contraseñas aleatorias:
'''
import random
import string

def generar_contrasena(longitud=12):
    # string.ascii_letters = 'abcdefg...XYZ'
    # string.digits = '0123456789'
    # string.punctuation = '!@#$%...'
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    for _ in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena

# Generar 5 contraseñas de diferentes longitudes
for longitud in [8, 12, 16, 20, 24]:
    print(f"  Longitud {longitud}: {generar_contrasena(longitud)}")
'''
Salida: 
  Longitud 8: lA]JYP3}
  Longitud 12: @jUPVa\{:I~@
  Longitud 16: i&uYbHMA*)M(Kmqp
  Longitud 20: ?a<!$6ev5dkrv0g?Ysa#
  Longitud 24: F;i"5>7k<3T{,z1)mt6'-?JC
'''
