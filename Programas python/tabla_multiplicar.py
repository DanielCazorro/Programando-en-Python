# Función de tabla de multiplicar, a la que le damos el número que queremos multiplicar
def tabla_multiplicar(numero):
    for tabla in range(1, 11):
        print("{:>2} x {} = {:>2}".format(tabla, numero, tabla*numero))
