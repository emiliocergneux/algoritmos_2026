def inver(texto):
    if len(texto) <= 1:
        return texto
    return inver(texto[1:]) + texto[0]

cadena = "ejercicio"
print(inver(cadena))