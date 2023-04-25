# Tasa autonómica
# Construye un programa que aplique una tasa a un precio en función de donde se aplique. Así si la provincia en la que se aplica es 'VA' (Valencia) se debe incrementar el precio en un 5, 5 % . En otro caso no se aplicará esta tasa. La salida debe ser distinta en función de la provincia, así:

# Si el precio es 10 €
# - Provincia = 'VA':
#     El subtotal es 10.00€
#     La tasa es 0.55€
#     El total es 10.55€

# - Provincia != 'VA':
#     El total es 10.00€
# Restricciones
# Implementar este programa usando sólo un if sin usar else
# Las cifras en € deben estar redondeadas al céntimo
# Utiliza una sola sentencia print para dar el resultado
# Retos
# Permitir al usuario introducir su provincia en mayúsculas, minúsculas o mixto
# Permitir al usuario introducir el nombre completo de su provincia en mayúsculas, minúsculas o mixto

porcentaje_provincias = {"VA": 0.55, "MA": 0.10}

subtotal = input("Introduzca el importe: ")
subtotal = float(subtotal)
pais = input("Introduzca la provincia: ")

tasa = subtotal * porcentaje_provincias[pais]

total = subtotal + tasa

print(
    f"El subotal es : {subtotal} €\nLa tasa es: {tasa} €\nEl total es: {total} €")
