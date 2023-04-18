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

    return contador
