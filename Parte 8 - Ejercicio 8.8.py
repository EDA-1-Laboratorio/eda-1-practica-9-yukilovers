'''
Ejercicio 8.8 — Completa el código
Completa el código que genera todas las combinaciones de dos dados y cuenta cuántas suman un valor dado:
'''

def contar_sumas(objetivo):
    conteo = 0
    combinaciones = []
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            if dado1 + dado2 == objetivo:
                conteo += 1
                combinaciones.append((dado1, dado2))
    return conteo, combinaciones

objetivo = 7
total, combos = contar_sumas(objetivo)
print(f"Formas de obtener {objetivo} con dos dados: {total}")
for c in combos:
    print(f"  {c[0]} + {c[1]} = {objetivo}")
