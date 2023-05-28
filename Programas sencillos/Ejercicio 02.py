# # Ejercicio 2. Boletín de notas

# ## Enunciado. 

# Crea una lista con 5 asignaturas. Después crea un programa que te pida la nota de cada asignatura mostrando el mensaje "Nota de <Asignatura>?"

# El programa debe, una vez introducidas todas la notas mostrar el boletín de notas según el siguiente esquema:
# ```

# --------------------------------------------
# Nombre de asignatura 1:                 10.0
# El nombre de la segunda:                 4.5
# nombre corto de 3                        6.8
# la cuarta                                7.5
# ultima asignatura                        5.0
# --------------------------------------------
# NOTA MEDIA                               6.8

# ```
# Es decir debes mostrar los nombres y notas ajustados, teniendo en cuenta que los nombres de las asignaturas tendrán longitudes diferentes. E igual con las notas.

# Debes además calcular y mostrar la media de las 5 notas y ajustarlo a un único decimal

#TODO: Falta alinear las cadenas salientes

subjectsList = ["Matemáticas", "Lengua", "Física", "Química", "Informática"]

def average():
    """
    Pide notas de asignaturas y devuelve la media
    """
    mathScore = int(input(f"Nota de {subjectsList[0]}:"))
    languageScore = int(input(f"Nota de {subjectsList[1]}:"))
    physicalScore = int(input(f"Nota de {subjectsList[2]}:"))
    chemistryScore = int(input(f"Nota de {subjectsList[3]}:"))
    computingScore = int(input(f"Nota de {subjectsList[4]}:"))

    averageScore = (mathScore + languageScore + physicalScore + chemistryScore + computingScore) / 5

    print(f"{subjectsList[0]}: {mathScore}\n{subjectsList[1]}: {languageScore}\n{subjectsList[2]}: {physicalScore}\n{subjectsList[3]}: {chemistryScore}\n{subjectsList[4]}: {computingScore}\nNOTA MEDIA: {averageScore:.1f}\n")

average()