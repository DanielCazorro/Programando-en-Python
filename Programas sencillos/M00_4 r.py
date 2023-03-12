# # Concatenando cadenas

# Crear un programa que pida nombre, verbo, adverbio y adjetivo y con ellos construya una historia. Utilizar una plantilla con los huecos donde colocar el nombre, el verbo, el adverbio y el adjetivo. Eligiendo bien la plantilla la frase puede resultar absurda y hasta graciosa.

# # Restricciones

# 1. Utilizar un solo print en el programa
# 2. Hacer una versión utilizando substitucion

# Retos

# 1. Introducir más datos para complicar y aumentar la historia
# 2. Construye una historia del estilo de los libros de * Construye tu propia aventura * de forma que la historia derive según se elija una u otra opción.

nombre = input("Escriba un nombre: ")
verbo = input("Escriba un verbo: ")
adverbio = input("Escriba un adverbio: ")
adjetivo = input("Escriba un adjetivo: ")

nombre2 = input("Introduzca otro nombre: ")
verbo2 = input("Escriba otro verbo: ")
adverbio2 = input("Escriba otro adverbio: ")
adjetivo2 = input("Escriba otro adjetivo: ")

print(
    f"Esta es la historia del {adjetivo} {nombre}. Su mayor virtud era poder {verbo} {adverbio} toda la noche. De repente, ve dos puerta, con números diferentes escritos. Una tenía el 22 y la otra el 41.")

camino = ""
while camino != '22' and camino != '41':
    camino = input("¿Por que puerta pasarás(22/41)?")

if camino == '41':
    print(
        f"Al pasar por la puerta vio un {adjetivo2} gato llamado {nombre2}. Ese gato iba a {verbo} {adverbio} cuando de repente todo se volvió negro y despertaste del sueño.")
elif camino == '22':
    print(
        f"Una ráfaga de aire frío pasó a tu alrededor, y viste una forma {adjetivo2} que se hacía llamar {nombre2}. Mientras te contaba que le gustaba {verbo2} {adverbio2} te iba arrastrando al pozo, del que nunca saldrás.")
