# Ejercicio 9

# Enunciado. Vasos reciclados
# Una fábrica produce vasos reciclados partiendo de vasos usados. Conociendo el número de vasos reciclados y cuandos de ellos se necesitan para obtener uno reciclado, crea una función que te diga el máximo de vasos que puedes conseguir de una cantidad cualquiera de vasos reciclados, reciclándolos sucesivas veces.

def vasosReciclados(vasos_recogidos, vasos_necesarios):

    vasos_fabricados = 0
    vasos_sobrantes = 0

    while vasos_recogidos != vasos_necesarios:
        vasos_reciclados = (vasos_recogidos//vasos_necesarios)
        vasos_sobrantes = (vasos_recogidos%vasos_necesarios)
        vasos_recogidos = vasos_reciclados + vasos_sobrantes

        vasos_fabricados += vasos_reciclados
    
    print(vasos_fabricados)
    return vasos_fabricados

vasosReciclados(70,4)