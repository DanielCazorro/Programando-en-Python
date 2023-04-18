def creaContador(ini=0):
    clicks = ini

    def click():
        nonlocal clicks
        clicks += 1
        return clicks

    return click


# Creador de la función con comportamiento y estado -> Clase
def creaContadorReutilizable(ini=0):
    '''
    Variables de estado -> Atributos
    '''
    clicks = ini

    '''
    reset, consulta, click
    Funcioens de comportamiento -> Métodos
    '''
    def reset(v):
        nonlocal clicks
        clicks = v
        return clicks

    def consulta():
        return clicks

    def click():
        nonlocal clicks
        clicks += 1
        return clicks

    '''
    Parte que crea lo necesario para que el contador funcione (infraestructura mínima) -> Constructor
    incluye el return
    '''
    def contador(**kwargs):
        nonlocal clicks

        if len(kwargs) == 0:
            return click()

        if 'consulta' in kwargs:
            return consulta()

        if 'reset' in kwargs:
            valor_inicial = kwargs['reset']
            return reset(valor_inicial)

        # raise Exception('Funcion desconocida')

    return contador


class Contador():
    def __init__(self, ini=0):
        self.clicks = ini

    def click(self):
        self.clicks += 1
        return self.clicks

    def consulta(self):
        return self.clicks

    def reset(self, v):
        self.clicks = v
        return self.clicks
