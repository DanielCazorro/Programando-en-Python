# Ejercicio 8. Es un palíndromo

# Enunciado
# Un palíndromo es una palabra o una frase que (ignorando los espacios, signos de puntuación y tildes) se lee igual al derecho que al revés.
# Debes crear una función que compruebe si una cadena es un palíndromo. No puedes utilizar la solución obvia de python cadena = cadena[::-1].
# Debes ignorar los espacios y para ignorar las mayúsculas y minúsculas y las tildes, empieza por poner la frase en minúsculas, sin tildes ni signos de puntuación
# Ejemplos de palíndromos

# ojo
# reconocer
# somos
# anita lava la tina
# dabale arroz a la zorra el abad

def es_palindromo(cadena):
    cadena = cadena.replace(" ", "")
    cadena = cadena.lower()

    return cadena == cadena[::-1]
