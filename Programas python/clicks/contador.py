def creaContador(ini=0):
    clicks = ini

    def click():
        nonlocal clicks
        clicks += 1
        return clicks

    return click


def creaContadorReutilizable(ini=0):
    clicks = ini

    def reset(v):
        nonlocal clicks
        clicks = v
        return clicks

    def consulta():
        return clicks

    def contador(**kwargs):
        nonlocal clicks

        if len(kwargs) == 0:
            clicks += 1
            return clicks

        if 'consulta' in kwargs:
            return consulta()

        if 'reset' in kwargs:
            valor_inicial = kwargs('reset')
            return reset(valor_inicial)

        # raise Exception('Funcion desconocida')

    return contador
