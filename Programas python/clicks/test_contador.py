from contador import creaContador, creaContadorReutilizable

click1 = creaContador()

click2 = creaContador(5)

clickR1 = creaContadorReutilizable()

clickR2 = creaContadorReutilizable(5)

print(click1(), clickR1(consulta=True), clickR1(), clickR1(consulta=True))  # 1

print(click2(), clickR2(consulta=True), clickR2(), clickR2(consulta=True))  # 6

clickR1()
clickR1()
clickR1()

print(clickR1(consulta=True))  # 4
print(clickR1(reset=0))  # print 0
print(clickR1(consulta=True))  # 0
print(clickR1())  # 1
