# Función es bisiesto

# Crear una función que como parámetro de entrada tenga un año y devuelva true si es bisiesto y false si no lo es.
# Condiciones de bisiesto
# Cualquier año divisible entre 400 es bisiesto
# De los restantes, cualquier año divisible entre 100 no es bisiesto
# De los restantes cualquier año divisible entre 4 es bisiesto
# Los demás no son bisiesto

def esBisiesto(year):
  return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) 