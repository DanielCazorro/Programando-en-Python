sueldos = (12450, 20200, 35200, 60000, 70000, 100000, 10000000)
retenciones = (1.55, 13.32, 20.08, 26.84, 29.91, 33.94, 44.88)

strMiSueldo = input("Introduce sueldo: ")
miSueldo = float(strMiSueldo)

ix = 0
while miSueldo >= sueldos[ix]:
    ix = ix + 1
