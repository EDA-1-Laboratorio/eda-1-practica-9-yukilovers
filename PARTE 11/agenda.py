'''
Ejercicio integrador B: Agenda de contactos
Crea un archivo agenda.py. Desarrolla una agenda telefónica que almacene contactos como diccionarios con llaves nombre, telefono, email. Implementa:

Agregar contacto
Listar contactos — Ordenados alfabéticamente por nombre
Buscar contacto — Búsqueda parcial (que el nombre contenga la cadena buscada)
Editar contacto — Permite cambiar teléfono o email
Eliminar contacto
Exportar — Imprime todos los contactos en formato CSV (separados por comas)
Estadísticas — Total de contactos, dominios de email más comunes
Salir
'''
def agregar_contacto(agenda):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    # TODO: Crear diccionario y agregarlo a la agenda
    contacto= {"nombre": nombre,"telefono": telefono, "email": email}
    agenda.append(contacto)
    print("Contacto agregado.")
    pass #no es necesario, pero lo dejare porque segun yo no afecta :D

def listar_contactos(agenda):
    if not agenda:
        print("Agenda vacía.")
        return
    # TODO: Ordenar por nombre e imprimir en formato tabular
    # Pista: sorted(agenda, key=lambda c: c["nombre"])
    agenda_ord=sorted(agenda, key=lambda contacto: contacto["nombre"].lower()) #cambie c por contacto, para facilitar mi comprension y 
                                                        #agrege lower por que las mayusculas tendria prioridad y no iria alfabeticamente
    print(f"\n{'Nombre':<15} {'Teléfono':<15} {'Email':<20}")
    print("-" * 50)
    for contacto in agenda_ord:
        print(f"{contacto['nombre']:<15} {contacto['telefono']:<15} {contacto['email']:<20}")
    pass

def buscar_contacto(agenda, termino):
    # TODO: Retornar lista de contactos cuyo nombre contenga 'termino'
    # Pista: usa 'termino.lower() in contacto["nombre"].lower()'
    resultados= [contacto for contacto in agenda if termino.lower() in contacto["nombre"].lower()]
    return resultados
    pass

def editar_contacto(agenda):
    nombre = input("Nombre del contacto a editar: ")
    resultados = buscar_contacto(agenda, nombre)
    if not resultados:
        print("No se encontró el contacto.")
        return
    # TODO: Si hay múltiples resultados, mostrarlos y pedir selección
    # TODO: Pedir nuevo teléfono y/o email (enter para no cambiar)
    contacto_a_editar=resultados[0]
    print(f"Editando a: {contacto_a_editar['nombre']}")
    nuevo_tel = input(f"Nuevo teléfono (Actual: {contacto_a_editar['telefono']}): ")
    nuevo_email = input(f"Nuevo email (Actual: {contacto_a_editar['email']}): ")
    if nuevo_tel: contacto_a_editar['telefono'] = nuevo_tel
    if nuevo_email: contacto_a_editar['email'] = nuevo_email
    print("Datos actualizados.")
    pass

def eliminar_contacto(agenda):
    nombre_borrar = input("Nombre del contacto a eliminar: ")
    # TODO: Buscar y eliminar
    for contacto in agenda:
        if contacto['nombre'].lower() == nombre_borrar.lower():
            agenda.remove(contacto)
            print(f"El contacto '{nombre_borrar}' ha sido eliminado.")
            return
    print("No se encontró el contacto.")
    pass

def exportar_csv(agenda):
    # TODO: Imprimir cada contacto como: nombre,telefono,email
    if not agenda:
        print("No hay nada que exportar.")
        return
    print("\n--- FORMATO CSV ---")
    print("nombre,telefono,email")
    for contacto in agenda:
        print(f"{contacto['nombre']},{contacto['telefono']},{contacto['email']}")
    pass

def estadisticas(agenda):
    # TODO: Total de contactos
    # TODO: Contar dominios de email (parte después del @)
    print(f"\nTotal de contactos: {len(agenda)}")
    dominios = {}
    for contacto in agenda:
        correo = contacto['email']
        if "@" in correo:
            dominio = correo.split('@')[-1]
            dominios[dominio] = dominios.get(dominio, 0) + 1
    
    print("Dominios más comunes:")
    for dominio, cantidad in dominios.items():
        print(f"  {dominio}: {cantidad}")
    pass

def menu():
    agenda = []
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Eliminar contacto")
        print("6. Exportar CSV")
        print("7. Estadísticas")
        print("8. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            listar_contactos(agenda)
        elif opcion == "3":
            termino = input("Buscar: ")
            resultados = buscar_contacto(agenda, termino)
            if resultados:
                for c in resultados:
                    print(f"  {c['nombre']} - {c['telefono']} - {c['email']}")
            else:
                print("Sin resultados.")
        elif opcion == "4":
            editar_contacto(agenda)
        elif opcion == "5":
            eliminar_contacto(agenda)
        elif opcion == "6":
            exportar_csv(agenda)
        elif opcion == "7":
            estadisticas(agenda)
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()
