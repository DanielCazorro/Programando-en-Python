class Alumno():

    def __init__(self, n, ap):
        self.nombre = n
        self.apellidos = ap
        self.movil = ''
        self.correo_e = ''

    def __str__(self):
        return 'Alumno: {} {} - {}'.format(self.nombre, self.apellidos, self.correo_e)

    def __repr__(self):
        return self.__str__()
