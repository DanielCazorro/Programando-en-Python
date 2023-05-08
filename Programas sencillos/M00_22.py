# # Solucionando problemas del coche
# # Hacer un programa que siga el siguiente arbol de decisiones para dar con el diagnóstico del problema de nuestro coche.


# # Por ejemplo:

# # ¿Arranca? S
# # ¿Suena un clic-clic? S

# # Entonces:
# # Reemplaza la batería
# # Restricciones
# # Realiza las preguntas relevantes según las respuestas del usuario
# # Retos
# # Investigar sobre árboles de decisión y como codificarlo sin hacerlo a capón como arriba

Respuesta = input("¿Arranca? ")
solucion = "Todo parece OK"
if Respuesta.lower() == 's':
  Respuesta = input("¿Suena un clic-clic? ")
  if Respuesta.lower() == 's':
    solucion = "Reemplaza la batería"
  else: 
    Respuesta = input("¿Se enciende el coche pero no arranca? ")
    if Respuesta.lower() == 's':
      solucion = "Revisa las bujías"
    else:
      Respuesta = input("¿Arranca el coche y luego se cala? ")
      if Respuesta.lower() == 's':
        Respuesta = input("¿Es un coche de inyección ")
        if Respuesta.lower() == 's':
          solucion = "Lleve el coche al taller"
        else:
          solucion = "Abra y cierre el starter"
else:
  Respuesta = input("¿Están los bornes de la batería corroidos? ")
  if Respuesta.lower() == 's':
    solucion = "Limpia los bornes y arranca de nuevo"
  else:
    solucion = "Reemplaza los cables y arranca de nuevo"

print("Entonces...\n", solucion)