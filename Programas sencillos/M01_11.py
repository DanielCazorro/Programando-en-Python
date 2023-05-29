# # Simular la tirada de dos dados

# Para simular una tirada de dados o cualquier otro hecho cuyo resultado se debe al azar utilizamos la librería [`random` ](https://docs.python.org/3.7/library/random.html)de python.

# En este caso necesitamos un programa que simule la tirada de dos dados mil veces y que nos devuelva la frecuencia de cada resultado para luego imprimirla.

# La mejor manera de hacerlo es un diccionario con los 11 resultados posibles, a saber, 2, 3, 4, 5, ..., 11 y 12.

# ## Restricciones

# - Mostrar una lista en pantalla con el valor de la combinación, la frecuencia aparecida en nuestra simulación en porcentaje, y el porcentaje previsto. Así:

# ```
# Total    Simulated    Expected
#            Percent     Percent
#    2          2.90        2.78
#    3          6.90        5.56
#    4          9.40        8.33
#    5         11.90       11.11
#    6         14.20       13.89
#    7         14.20       16.67
#    8         15.00       13.89
#    9         10.50       11.11
#   10          7.90        8.33
#   11          4.50        5.56
#   12          2.60        2.78
# ```

from random import randint

def twoDices():
  return randint(1,6)+randint(1,6)

frecuencies = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
expected = {2:2.78, 3:5.56, 4:8.33, 5:11.11, 6:13.89, 7:16.67, 8:13.89, 9:11.11, 10:8.33, 11:5.56, 12:2.78}

numOfRolls = 1000

for _ in range(0,numOfRolls):
  roll = twoDices()
  frecuencies[roll] += 1
  
print("Total\tSimulated\tExpected")
print("\t  Percent\t Percent")

for dice in frecuencies:
  print("{:5d}\t{:9.2f}\t{:8.2f}".format(dice, frecuencies[dice]/numOfRolls*100, expected[dice]))