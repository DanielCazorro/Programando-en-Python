# Calcular el porcentaje de retención para el IRPF en función de mi sueldo y circunstancias

# Obtención de datos
sueldo = float(input("Sueldo: "))
situacion = input("Situación (1/2/3) ")
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

# Obtener retencion

if sueldo_a_retener <= 12450:
    porcentaje = 19
elif sueldo_a_retener <= 20199:
    porcentaje = 24
elif sueldo_a_retener <= 35199:
    porcentaje = 30
elif sueldo_a_retener <= 59999:
    porcentaje = 37
elif sueldo_a_retener <= 299999:
    porcentaje = 45
else:
    porcentaje = 47

monton_anual = sueldo_a_retener * porcentaje/100
monto_mensual = monton_anual/12

# Mostramos resultados
print("Sueldo anual: \t", sueldo)
print("Situación: \t", situacion)
print("Base a retener: \t", sueldo_a_retener)
print("Porcentaje: \t", porcentaje)
print("Total anual: \t", monton_anual)
print("Retención mensual: \t", monto_mensual)
