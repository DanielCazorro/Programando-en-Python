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

    """
        self.asignaturas = []

    def alta_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise Exception(
                '{} debe ser del tipo Asignatura'.format(asignatura))

        if not asignatura in self.asignaturas():
            self.asignaturas.append(asignatura)

    """

    def __str__(self):
        return 'Alumno: {} {} - {}'.format(self.nombre, self.apellidos, self.correo_e)

    def __repr__(self):
        return self.__str__()
