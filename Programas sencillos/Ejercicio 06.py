# Ejercicio 6. Jerigonza

# Enunciado
# Jerigonza es una variante lúdica del español que consiste en añadir, en nuestro caso, la sílaba pi despues de cada vocal de una palabra en español.
# Construye un programa que pida una frase al usuario y que la transforme en jerigonza, imprimiéndola debajo.

def jerigonza():
    """
    Añade pi a cada vocal
    """
    finalPhrase = ""
    phrase = input("Escriba su frase: ")
    vocalList = "AEIOUaeiou"

    phraseToWork = list(phrase)

    for word in phraseToWork:
        if word in vocalList:
            word += "pi"
            finalPhrase += word
        else:
            finalPhrase += word
    
    print(finalPhrase)
    return finalPhrase

jerigonza()