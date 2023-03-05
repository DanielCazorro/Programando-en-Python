import IRPF2018

strMiSueldo = input("Introduce sueldo: ")
miSueldo = float(strMiSueldo)

# Búsqueda de límites
retenicion = IRPF2018.buscaRetencion(miSueldo)

# Cálculo de pagas
miSueldoNeto = IRPF2018.netoAnual(miSueldo, retenicion)

mensual12 = miSueldoNeto/12
mensual14 = miSueldoNeto/14

print(f"Mi sueldo neto: {miSueldoNeto}")
print(f"12 pagas de: {mensual12}")
print(f"14 pagas de: {mensual14}")
