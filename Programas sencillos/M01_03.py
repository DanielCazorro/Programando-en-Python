# Crear funcion replace
# Crear una función que tome una cadena y remplace el caracter de una posición dada por otro según la definición

#  myReplace(cadena, posicion, nuevoValor)
# Restricciones
# Teniendo en cuenta que en python una cadena es realmente una tupla de caracteres (inmutable, no se puede modificar ni su longitud, ni su contenido) deberás valorar crear una nueva cadena con el resultado y devolverla.
# Crear un módulo reutilizable. Para hacerlo correctamente (incluyendo la distinción entre utilizarlo como módulo o como main - no visto aún en clase - mira aquí)

def myReplace(cadena, posicion, nuevoValor):
    indice = 0
    resultado = ""
    while indice < len(cadena):
        if indice == posicion:
            resultado += nuevoValor
        else:
            resultado += cadena[indice]
        
        indice += 1

    return resultado
    