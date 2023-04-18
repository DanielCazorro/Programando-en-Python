def creaContador(ini=0):
    clicks = ini

    def click():
        nonlocal clicks
        clicks += 1
        return clicks

    return click


def creaContadorReutilizable(ini=0):
    pass
