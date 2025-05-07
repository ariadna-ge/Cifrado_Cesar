def cifra_cesar(cadena, llave):
    """Realiza el cifrado César sobre una cadena de texto con la llave dada."""
    if llave < 0:
        llave = 26 - (-llave % 26)

    nuevaCadena = ""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_mayus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for l in cadena:
        if l in alfabeto:
            posicionLetra = alfabeto.index(l)
            nuevaCadena += alfabeto[(posicionLetra + llave) % 26]
        elif l in alfabeto_mayus:
            posicionLetra = alfabeto_mayus.index(l)
            nuevaCadena += alfabeto_mayus[(posicionLetra + llave) % 26]
        else:
            nuevaCadena += l
    return nuevaCadena