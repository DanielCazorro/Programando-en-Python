# # Listando códigos ascii

# Crear un programa que devuelva los códigos ASCII de los carácteres desde el 32 al 127.

# ## Restricciones
# - Formatear la salida en cuantro columnas perfectamente alineadas. Puedes ayudarte con [format](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3) y [print](https://docs.python.org/3/library/functions.html#print)

for character in range(32, 128):
  print("'{}': {:3d}".format(chr(character), character), end="\t")
  if character % 4 == 3:
    print("")