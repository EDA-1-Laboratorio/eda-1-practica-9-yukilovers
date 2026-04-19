def separar_palabras(texto):
    lista_palabras = texto.split()
    return lista_palabras

def contar_palabras(texto):
    # TODO: Retornar el número total de palabras
    palabras = separar_palabras(texto)
    cantidad_palabras = len(palabras)
    return cantidad_palabras

def contar_oraciones(texto):
    # TODO: Contar oraciones (terminan en '.', '!' o '?')
    ##El menos 1 quita las oraciones extras que ya no incluyen esa terminacion
    cant_fin_oraciones_coma = len(texto.split(","))-1
    cant_fin_oraciones_punto = len(texto.split("."))-1
    cant_fin_oraciones_exclamacion = len(texto.split("!"))-1
    cant_fin_oraciones_interrogacion = len(texto.split("?"))-1

    cantidad_oraciones = cant_fin_oraciones_punto + cant_fin_oraciones_coma + cant_fin_oraciones_exclamacion + cant_fin_oraciones_interrogacion
    return cantidad_oraciones    

def palabra_mas_frecuente(texto):
    # TODO: Retornar la palabra que más se repite (ignorar mayúsculas)
    # Pista: usa un diccionario para contar frecuencias
    palabras = separar_palabras(texto)
    palabras_minusculas = [pal.lower() for pal in palabras]
    frecuencias = {}

    for palb in palabras_minusculas:
        if palb in frecuencias:
            frecuencias[palb]  += 1
        else:
            frecuencias[palb] = 1

    mas_frecuente = max(frecuencias, key=frecuencias.get)

    return mas_frecuente.capitalize()

def palabras_unicas(texto):
    # TODO: Retornar un conjunto (set) de palabras únicas
    set_unicas = set(separar_palabras(texto))
    
    return set_unicas

def longitud_promedio_palabras(texto):
    # TODO: Retornar la longitud promedio de las palabras
    lista_de_palabras = separar_palabras(texto)
    total_letras = 0
    promedio_palabra = 0

    for pal in lista_de_palabras:
        total_letras += len(pal)
    
    promedio_palabra = total_letras/len(lista_de_palabras)
        
    return round(promedio_palabra, 2)

def buscar_palabra(texto, palabra):
    # TODO: Retornar cuántas veces aparece la palabra en el texto
    lista_palabras = separar_palabras(texto)
    cantidad_palabra = 0
    for pal in lista_palabras:
        if pal == palabra: cantidad_palabra += 1

    return cantidad_palabra

def reemplazar_palabra(texto, vieja, nueva):
    # TODO: Retornar el texto con la palabra vieja reemplazada por la nueva
    lista_palabras = separar_palabras(texto)
    nueva_lista = []
    oracion_reemplazada = ""

    for pal in lista_palabras:
        if pal == vieja: 
            nueva_lista.append(nueva)
        else: nueva_lista.append(pal)
    
    oracion_reemplazada = " ".join(nueva_lista)
    return oracion_reemplazada

# Texto de ejemplo para analizar
texto_ejemplo = """
Python es un lenguaje de programación muy popular. Python es fácil de aprender.
Muchos programadores usan Python para ciencia de datos y para desarrollo web.
Python tiene una gran comunidad. La comunidad de Python es muy activa y amigable.
¿Te gusta programar? ¡Python es una excelente opción para empezar!
"""

print("=== ANALIZADOR DE TEXTO ===")
print(f"Total de palabras: {contar_palabras(texto_ejemplo)}")
print(f"Total de oraciones: {contar_oraciones(texto_ejemplo)}")
print(f"Palabra más frecuente: {palabra_mas_frecuente(texto_ejemplo)}")
print(f"Palabras únicas: {len(palabras_unicas(texto_ejemplo))}")
print(f"Longitud promedio: {longitud_promedio_palabras(texto_ejemplo):.1f}")
print(f"Veces que aparece 'Python': {buscar_palabra(texto_ejemplo, 'Python')}")

nuevo = reemplazar_palabra(texto_ejemplo, "Python", "Java")
print(f"\nTexto modificado (primeras 100 letras):\n{nuevo[:100]}...")

