lista = list()
while True:
    n = int(input('Digite um valor.'))  #colocar um valor em input como  n =
    if n not in lista:  #dificuldade aqui para lembrar.
        lista.append(n) #essa parte da lista pra add n ai os numeros não fica duplicados
        print('Valor adicionado com sucesso.')
    else:
        print('Valor Duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':  #aqui foi suave lembrei de tudo.
        resp = str(input('DESEJA CONTINUAR ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('==-' * 30)
lista.sort() #colocar o sort uma linha antes da onde eu quero organizar. de vez colocar no topo.
print(f'Você digitou os seguintes números {lista}')