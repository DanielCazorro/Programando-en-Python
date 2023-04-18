from academia import Alumno, Asignatura, Profesor

roberto = Alumno('Roberto', 'Rodríguez')
susana = Alumno('Susana', 'Martín')

print(roberto.nombre, roberto.apellidos, roberto)  # Roberto Rodríguez
print(susana.nombre, susana.apellidos, susana)  # Susana Martín

print(roberto.correo_e, roberto.movil)

ingles = Asignatura("Inglés", "A2")
ingles.precio_h = 7.5
aleman = Asignatura('Aleman', 'A2')
aleman.precio_h = 8
chino = Asignatura('Chino Cantonés', 'A1')
chino.precio_h = 10

print(ingles)  # Asignatura: Inglés - A2 - (30.00 €/mes)

roberto.alta_asignatura(ingles)
roberto.alta_asignatura(chino)

# [Asignatura: Inglés - A2 - (30.00 €/mes), Asignatura: Chino....]
print(roberto.asignaturas)
print(susana.asignaturas)

donJose = Profesor("Jose", "Martín Fusta", "0W", "jf@gmail.com")
print(donJose)  # Profesor: 0W - José Martín Fusta - jf@gmail.com

print(donJose.sueldo())  # 200

donJose.alta_asignatura(ingles)

print(donJose.asignaturas)  # [Asignatura: Inglés - A2 - (30.00 €/mes)]
print(donJose.sueldo())
