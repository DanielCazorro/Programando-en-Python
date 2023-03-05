nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)

StrEdad = input("¿Cuántos años tienes? ")
edad = int(StrEdad)

StrA_actual = input("¿En qué año estamos? ")
a_actual = int(StrA_actual)

a_nacimiento = a_actual - edad

print(nombre, "naciste en", a_nacimiento)
