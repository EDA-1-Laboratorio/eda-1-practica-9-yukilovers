'''
Escribe y ejecuta el siguiente código que muestra el operador ternario (expresión condicional) de Python:
'''

# En C:  resultado = (condicion) ? valor_verdadero : valor_falso;
# En Python:
edad = 20
estado = "Mayor" if edad >= 18 else "Menor"
print(estado)   # Mayor

# Otro ejemplo: valor absoluto
n = -7
absoluto = n if n >= 0 else -n
print(f"|{n}| = {absoluto}")   # |-7| = 7

# Útil dentro de print
nota = 8.5
print(f"Resultado: {'Aprobado' if nota >= 6 else 'Reprobado'}")

# Varios valores
hora = 14
saludo = "Buenos días" if hora < 12 else "Buenas tardes" if hora < 20 else "Buenas noches"
print(saludo)   # Buenas tardes

'''
Ejecución del código en python:

Mayor
|-7| = 7
Resultado: Aprobado
Buenas tardes

'''
