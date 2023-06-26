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
def teste(b):
    b += 4 # > aqui passa valer 9
    c = 2 # > na caso b e c só funciona nessa area que seria o Escopo Local
    print(f'A Dentro de vale(a)') # > 5
    print(f'B Dentro de vale(b)') # > 9
    print(f'C Dentro de vale(c)') # > 2

# > enquanto o A ele pega essa area global inteira.
a = 5 # > o que esta aqui é um Escopo Global
teste(a)

# > =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# > Retorno de Resultados.
# > ou return
def soma(a=0, b=0, c=0):
    s = a + b + c
    return{s}

r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)
print(f'Os Resultados foram {r1}, {r2} e {r3}')

