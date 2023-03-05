# Calcular el porcentaje de retención para el IRPF en función de mi sueldo y circunstancias

# Obtención de datos
sueldo = float(input("Sueldo: "))
situacion = input("Situación (1/2/3)")
num_hijos = int(input("Número de hijos: "))

# Calcular exención
exencion = 0
if situacion == '1':
    if num_hijos <= 0:
        exencion = 0
    elif num_hijos == 1:
        exencion = 17270
    else:
        exencion = 18617

if situacion == '2':
    if num_hijos <= 0:
        exencion = 16696
    elif num_hijos == 1:
        exencion = 17894
    else:
        exencion = 19241

if situacion == '3':
    if num_hijos <= 0:
        exencion = 15000
    elif num_hijos == 1:
        exencion = 15599
    else:
        exencion = 16272

sueldo_a_retener = sueldo - exencion
