def extraer_vocales(palabra):
    vocales = ''
    for caracter in palabra:
        if caracter.upper() in 'AEIOU':
            vocales += caracter
    print(f"Las vocales de su palabra {palabra} son: {vocales}")

    return vocales
