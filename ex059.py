n1 = int(input('Primeiro Valor.'))
n2 = int(input('Segundo Valor.'))
opção = 0
while opção != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('Qual a sua Opção? '))
    if opção == 1:
        soma = n1 + n2
        print('o resultado de {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicar = n1 * n2
        print('o resultado é de {} * {} é {}'.format(n1, n2, multiplicar))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior é {} '.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os numeros novemente.')
        n1 = int(input('Primeiro Valor'))
        n2 = int(input('Segundo Valor'))
    elif opção == 5:
        print('Finalizado')
    else:
        print('Opção invalida tente novamente')
    print('====' * 10)
print('Fim Do Programa.')
