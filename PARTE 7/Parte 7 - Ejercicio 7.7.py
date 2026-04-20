'''
¿Cuál es el equivalente en Python de la siguiente estructura en C?

switch(opcion) {
    case 1: printf("Uno"); break;
    case 2: printf("Dos"); break;
    default: printf("Otro"); break;
}

    a)

    switch opcion:
        case 1: print("Uno")
        case 2: print("Dos")
        default: print("Otro")

    b)

    if opcion == 1:
        print("Uno")
    elif opcion == 2:
        print("Dos")
    else:
        print("Otro")

    c)

    match opcion:
        case 1: print("Uno")
        case 2: print("Dos")
        case _: print("Otro")

    d) Tanto b) como c) son válidas (c a partir de Python 3.10)

Respuesta: d)
'''
