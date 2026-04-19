'''
Ejercicio 6.12 — Variables globales y locales (III)
Estudia el siguiente código y sin ejecutarlo, predice qué se imprime:
'''

def exterior():
    mensaje = "hola"

    def interior():
        print("Interior:", mensaje)

    interior()
    print("Exterior:", mensaje)

exterior()
#print(mensaje)  # ¿Qué pasaría si descomentas esta línea?

'''
Tu predicción:

Interior: hola
Exterior: hola
Si descomentas print(mensaje): Error
'''
