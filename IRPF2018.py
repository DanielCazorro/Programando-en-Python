sueldos = (12450, 20200, 35200, 60000, 70000, 100000, 10000000)
retenciones = (1.55, 13.32, 20.08, 26.84, 29.91, 33.94, 44.88)


def buscaRetencion(s):
    ix = 0
    while ix < 7 and s >= sueldos[ix]:
        ix = ix + 1

    if ix == 0:
        retencion = 0
    elif ix == 7:
        retencion = 45
    else:
        retencion = retenciones[ix - 1] + ((s - sueldos[ix - 1]) * (
            retenciones[ix] - retenciones[ix - 1]) / (sueldos[ix] - sueldos[ix - 1]))

    return retencion


def netoAnual(r):

    retencionTotal = r + 6.35

    miSueldoNeto = miSueldo * (100-retencionTotal)/100

    return miSueldoNeto
