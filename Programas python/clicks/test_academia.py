from academia import Alumno, Asignatura

roberto = Alumno('Roberto', 'Rodríguez')
susana = Alumno('Susana', 'Martín')

print(roberto.nombre, roberto.apellidos, roberto)  # Roberto Rodríguez
print(susana.nombre, susana.apellidos, susana)  # Susana Martín

print(roberto.correo_e, roberto.movil)

ingles = Asignatura("Inglés", "A2")
ingles.precio_h = 7.5

print(ingles)  # Asignatura: Inglés - A2 - (30.00 €/mes)

roberto.alta_asignatura(ingles)

print(roberto.asignatura)  # Asignatura: Inglés - A2 - (30.00 €/mes)
print(susana.asignatura)

roberto.asignatura = None
print(roberto.asignatura)
