'''
opciones 

    a) Cambia la H por h y texto ahora vale "hola"
    b) Se genera un error porque las cadenas son inmutables
    c) Se crea una nueva cadena "hola" automáticamente
    d) No pasa nada, el cambio se ignora silenciosamente

'''
texto = "Hola"
texto[0] = "h"

print(texto)

#Lo que sucede es lo descrito en el inciso  b) Se genera un error porque las cadenas son inmutables
