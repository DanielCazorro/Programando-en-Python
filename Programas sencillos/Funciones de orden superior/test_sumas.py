from sumas import sumaTodos, sumaTodosAlCuadrado, sumatorio

print(sumaTodos(100), sumatorio(100))  # 5050


def cuadrado(x):
    return x ** 2


print(sumaTodosAlCuadrado(3), sumatorio(3, cuadrado))  # 14
