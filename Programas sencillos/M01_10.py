# # Escribir un programa que traduzca a código Morse

# Utilizando un diccionario y el control de la pantalla desarrollado en screen. Escribir un programa que traduzca a Morse.

# ## Restricciones
# - El programa pedira una línea de texto y la traducirá a morse.
# - El programa seguirá pidiendo líneas hasta que se introduzca una cadena vacía. Entonces dejará de pedir lineas
# - El formato de salida debe ser tal que 
#   - Se impriman tantas líneas como se han introducido
#   - No se imprima nada entre las líneas (controlar la posición del input)

# | Carácter | Código | Carácter | Código | Carácter | Código |
# |---|---|---|---|
# |**A**|· —|**N**|— ·|**0**|— — — — —||
# |**B**|— · · ·|**Ñ**|— — · — —|**1**|· — — — —||
# |**C**|— · — ·|**O**|— — —|**2**|· · — — —||
# |**CH**|— — — —|**P**|· — — ·|**3**|· · · — —||
# |**D**|— · ·|**Q**|— — · —|**4**|· · · · —||
# |**E**|·|**R**|· — ·|**5**|· · · · ·||
# |**F**|· · — ·|**S**|· · ·|**6**|— · · · ·||
# |**G**|— — ·|**T**|—|**7**|— — · · ·||
# |**H**|· · · ·|**U**|· · —|**8**|— — — · ·||
# |**I**|· ·|**V**|· · · —|**9**|— — — — ·||
# |**J**|· — — —|**W**|· — —|**.**|· — · — · —||
# |**K**|— · —|**X**|— · · —|**,**|— · — · — —||
# |**L**|· — · ·|**Y**|— · — —|**?**|· · — — · ·||
# |**M**|— —|**Z**|— — · ·|**"**|· — · · — ·
# |**!**|— — · · — —||||||

morse = {
    'A': '· —',
    'B': '— · · ·',
    'C': '— · — ·',
    'CH': '— — — —',
    'D': '— · ·',
    'E': '·',
    'F': '· · — ·',
    'G': '— — ·',
    'H': '· · · ·',
    'I': '· ·',
    'J': '· — — —',
    'K': '— · —',
    'L': '· — · ·',
    'M': '— —',
    'N': '— ·',
    'Ñ': '— — · — —',
    'O': '— — —',
    'P': '· — — ·',
    'Q': '— — · —',
    'R': '· — ·',
    'S': '· · ·',
    'T': '—',
    'U': '· · —',
    'V': '· · · —',
    'W': '· — —',
    'X': '— · · —',
    'Y': '— · — —',
    'Z': '— — · ·',
    '0': '— — — — —',
    '1': '· — — — —',
    '2': '· · — — —',
    '3': '· · · — —',
    '4': '· · · · —',
    '5': '· · · · ·',
    '6': '— · · · ·',
    '7': '— — · · ·',
    '8': '— — — · ·',
    '9': '— — — — ·',
    '.': '· — · — · —',
    ',': '— · — · — —',
    '?': '· · — — · ·',
    '"': '· — · · — ·',
    '!': '— — · · — —',
    ' ': ' '
}

frase = input("Texto: ")

fraseMorse = ""
for caracter in frase:
  caracter = caracter.upper()
  if caracter not in morse:
    fraseMorse += 'X'
  else:
    fraseMorse += morse[caracter]

print(fraseMorse)