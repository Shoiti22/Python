from math import factorial

def fatorial(n, show=False):
    """
    -> CALCULA FATORIAL DE UM NUMERO.
    :param n: O Número a ser calculado
    :param show: Opcinal mostra  ou não a conta.
    :return: valor fatorial de um número.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa Principal
print(fatorial(5, show=False))