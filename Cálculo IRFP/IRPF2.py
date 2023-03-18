# Calcular el porcentaje de retención para el IRPF en función de mi sueldo y circunstancias

def obtener_exencion(sit, nhijos):

    exencion = 0
    if sit == '1':
        if nhijos <= 0:
            exencion = 0
        elif nhijos == 1:
            exencion = 17270
        else:
            exencion = 18617

    if sit == '2':
        if nhijos <= 0:
            exencion = 16696
        elif nhijos == 1:
            exencion = 17894
        else:
            exencion = 19241

    if sit == '3':
        if nhijos <= 0:
            exencion = 15000
        elif nhijos == 1:
            exencion = 15599
        else:
            exencion = 16272

    return exencion


def obtener_retencion(base):
    if base <= 0:
        porcentaje = 0
    elif base <= 12450:
        porcentaje = 19
    elif base <= 20199:
        porcentaje = 24
    elif base <= 35199:
        porcentaje = 30
    elif base <= 59999:
        porcentaje = 37
    elif base <= 299999:
        porcentaje = 45
    else:
        porcentaje = 47

    return porcentaje


    # Obtención de datos
sueldo = float(input("Sueldo: "))
situacion = input("Situación (1/2/3) ")
num_hijos = int(input("Número de hijos: "))

# Calcular exención

exencion = obtener_exencion(situacion, num_hijos)

sueldo_a_retener = sueldo - exencion

# Obtener retencion

porcentaje = obtener_retencion(sueldo_a_retener)

monton_anual = sueldo_a_retener * porcentaje/100
monto_mensual = monton_anual/12

# Mostramos resultados
print("Sueldo anual: \t", sueldo)
print("Situación: \t", situacion)
print("Base a retener: \t", sueldo_a_retener)
print("Porcentaje: \t", porcentaje)
print("Total anual: \t", monton_anual)
print("Retención mensual: \t", monto_mensual)
