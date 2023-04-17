from sumas import sumatorio


def sumatorioR(n):
    if n <= 0:
        return 0
    else:
        return n + sumatorioR(n - 1)


def sumaorioR_funcion(n, f):
    if n <= 0:
        return f(0)
    else:
        return n + sumaorioR_funcion(n - 1, f)


print(sumatorioR(100), sumatorio(100))
