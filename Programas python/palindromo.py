def es_palindromo(cadena):
    cadena = cadena.replace(" ", "")
    cadena = cadena.lower()

    return cadena == cadena[::-1]
