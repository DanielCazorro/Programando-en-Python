def creaContador(ini=0):
    clicks = ini

    def click():
        nonlocal clicks
        clicks += 1
        return clicks

    return click


def creaContadorReutilizable(ini=0):
    clicks = ini

    def contador(**kwargs):
        nonlocal clicks

        if len(kwargs) == 0:
            clicks += 1
            return clicks

        if 'consulta' in kwargs:
            return clicks

        if 'reset' in kwargs:
            # Aquí se puede validar que kwargs['reset'] sea >= 0 y entero
            clicks = kwargs['reset']
            print('Reseteado a', clicks)
            return clicks

    return contador
