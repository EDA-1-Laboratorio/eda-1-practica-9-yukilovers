'''
Completa un programa que simula un juego de adivinanza:
'''

import random

def juego_adivinanza():
    secreto = random.randint(1, 100)
    intentos = 0

    print("Adivina el número entre 1 y 100")

    while True:
        intento = int(input("Tu intento: "))
        intentos += 1

        if intento ==secreto:
            print("¡Correcto! Lo lograste en", intentos, "intentos")
            break     # terminar el ciclo
        elif intento < secreto:
            print("Demasiado bajo")
        else:
            print("Demasiado alto")

juego_adivinanza()

