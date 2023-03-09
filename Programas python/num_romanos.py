romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for clave, valor in romanos.items():
    print(f"{clave}:\t{valor}".rjust(3))
