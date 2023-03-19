from f_retenciones import obtener_exencion, obtener_retencion

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
