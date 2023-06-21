# > Veremos Interactive Help.
# > para usar basta colocar help() isso se chama função ou método.
# > podemos usar ex: help(print) aparece todas funçoes do print
# > =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# > Docstrings.
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Inicio da contagem.
    :param f: Fim da contagem.
    :param p: Passo da contagem.
    :return: sem retorno.
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM')
help(contador)

# > =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# >Parametros Opcionais.
# > Para usar esse Parametros devera fazer o seguinte ex:
def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é {s}')
soma(3, 2, 5)
soma(8, 4)
soma()
# > assim mesmo que não tenha um valor ele vai valer 0 e não dara erro.
# > =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# > Escopo de Variáveis.

# > é o local onde uma variavel vai existir ou não vai mais existir.


# > Retorno de Resultados.
