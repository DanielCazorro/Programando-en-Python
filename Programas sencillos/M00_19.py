# IVA general por paises
# Según el pais se aplica un tipo general de IVA u otro. Haz un programa que aplique el tipo de iva adecuado según el pais de origen

# Seguir la siguiente tabla. El programa debe mostrar la base, el iva aplicado en % y en € y el precio final.

# Restricciones
# Las cantidades en € deben aparecer ajustadas al céntimo
# Utilizar una sola instrucción de impresión de resultados


ivas = {
    "hungria": 27,
    "croacia": 25,
    "dinamarca": 25,
    "suecia": 25,
    "finlandia": 24,
    "rumania": 24,
    "grecia": 23,
    "irlanda": 23,
    "polonia": 23,
    "portugal": 23,
    "eslovenia": 22,
    "italia": 22,
    "españa": 21,
    "belgica": 21,
    "letonia": 21,
    "lituania": 21,
    "paises bajos": 21,
    "republica checa": 21,
    "austria": 20,
    "bulgaria": 20,
    "eslovaquia": 20,
    "estonia": 20,
    "francia": 20,
    "reino unido": 20,
    "alemania": 19,
    "chipre": 19,
    "malta": 18,
    "luxemburgo": 19
}

pais = input("Pais de origen: ")

precio = input("Precio: ")
precio = float(precio)

iva = precio * (ivas[pais.lower()]/100)

total = precio + iva

print(
    f"Base: {precio:0.2f}€\nIVA: {ivas[pais.lower()]}% + {iva:0.2f}€\nTotal: {total:0.2f}€")
