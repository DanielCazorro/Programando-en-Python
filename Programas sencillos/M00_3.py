# # Imprimiendo comillas

# Construir un programa que pida una cita y un autor y devuelva una única cadena con la cita entre comillas y el autor.

# ## Restricciones

# 1. No usar format ni % ni fstring.Hacerlo concatenando cadenas y escapando caracteres

cita = input("Escriba la cita deseada: ")
autor = input("Escriba el autor de su cita: ")

print("La cita:'", cita, "', pertenece al autor:'", autor, "'.")
