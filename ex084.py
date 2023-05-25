cadastro = list()
dados = list()
pesado = leve = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas cadastradas são {len(cadastro)}') #USAR O LEN PARA SABER O TOTAL DE PESSOAS
print(f' O Maior peso foi de {pesado} Kg. peso de ', end='')
for p in cadastro:
    if p[1] == pesado:
        print(f' [{p[0]}]', end='')
print('')
print(f' O Menor peso foi de {leve} Kg peso de ', end='')
for p in cadastro:
    if p[1] == leve:
        print(f' [{p[0]}]', end='')
print('')