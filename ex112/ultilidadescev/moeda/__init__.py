def aumentar(preço=0, taxa=0, formato=False):
    '''
    :param preço: o preço que quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato:quer a saida formatada ou não
    :return: o valor reajustado com ou sem o formato.
    '''
    res =  preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res =  preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'. center(30))
    print('-' * 30)
    print(f'Preço Analisado:\t{moeda(preço)}')
    print(f'Dobro do Preço: \t{dobro(preço, True)}')
    print(f'Metade do Preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% redução:  \t\t{diminuir(preço, taxar, True)}')
    print('-' * 30)