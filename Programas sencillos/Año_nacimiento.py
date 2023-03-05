# Pedimos el nombre
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)

# Pedimos la edad y la convertimos a int
StrEdad = input("¿Cuántos años tienes? ")
edad = int(StrEdad)

# Pedimos el año actual y lo convertimos a int
StrA_actual = input("¿En qué año estamos? ")
a_actual = int(StrA_actual)

# Realizamos el cálculo
a_nacimiento = a_actual - edad

# Mostramos el resultado
print(nombre, "naciste en", a_nacimiento)
