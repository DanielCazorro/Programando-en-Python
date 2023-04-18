class Asignatura():
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
        self.hora = 0

    def __str__(self):
        return 'Asignatura: {} - {} ({:.2f} €/mes)'.format(self.nombre, self.nivel, self.precio_h * 4)

    def __repr__(self):
        return self.__str__()


class Alumno():

    def __init__(self, n, ap):
        self.nombre = n
        self.apellidos = ap
        self.movil = ''
        self.correo_e = ''

        self.asignaturas = []

    def alta_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise Exception(
                '{} debe ser del tipo Asignatura'.format(asignatura))

        self.asignaturas.append(asignatura)

    def __str__(self):
        return 'Alumno: {} {} - {}'.format(self.nombre, self.apellidos, self.correo_e)

    def __repr__(self):
        return self.__str__()


class Profesor():
    def __init__(self, n, ap, nif, correo_e, sueldo_base=200):
        self.nombre = n
        self.apellidos = ap
        self.nif = nif
        self.movil = ''
        self.sueldo_base = sueldo_base
        self.correo_e = correo_e

        self.asignaturas = []

    def alta_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise Exception(
                '{} debe ser del tipo Asignatura'.format(asignatura))

        self.asignaturas.append(asignatura)

    def __str__(self):
        return 'Profesor: {} - {} {} - {}'.format(self.nif, self.nombre, self.apellidos, self.correo_e)

    def __repr__(self):
        return self.__str__()

    @property  # Esto es un decorador que transforma en una propiedad
    def sueldo(self):
        return self.sueldo_base + len(self.asignaturas) * 300
