# # Ejercicio 11. Una tabla de multiplicación universal.

# ## Enunciado

# Se trata de imprimir una tabla de multiplicar de todos los enteros desde 1 a 10 multiplicados por 1 a 10 de manera que en un vistazo en columnas y filas se ven todas las tablas.

# Debe quedar algo así

# ```
#        1   2   3   4   5   6   7   8   9  10
#    1   1   2   3   4   5   6   7   8   9  10
#    2   2   4   6   8  10  12  14  16  18  20
#    3   3   6   9  12  15  18  21  24  27  30
#    4   4   8  12  16  20  24  28  32  36  40
#    5   5  10  15  20  25  30  35  40  45  50
#    6   6  12  18  24  30  36  42  48  54  60
#    8   8  16  24  32  40  48  56  64  72  80
#    9   9  18  27  36  45  54  63  72  81  90
#   10  10  20  30  40  50  60  70  80  90 100  
# ```
# `

 #TODO: 
tabla1 = [1,2,3,4,5,6,7,8,9,10]

tabla2 = []
for number in tabla1:
    tabla2.append(number*2)

print(tabla1, end= 10)