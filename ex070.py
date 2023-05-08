total1000 = menorpreço = total = cont = 0
barato = ' '
while True:
    produto = str(input('NOME DO PRODUTO : '))
    preço = int(input('PREÇO R$ : '))
    total += preço #FACIL PORÉM TINHA ESQUECIDO COMO CALCULAR TOTAL.
    cont += 1
    if preço >= 1000:  #FOI FACIL
        total1000 += 1
    if cont == 1: #FOI DIFICIL ESQUECI COMO FAZIA. COMO DESCOBRIR O MENOR PREÇO
        menorpreço = preço
        barato = produto
    else:
        if preço < menorpreço:
            menorpreço = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('========= FIM DO PROGRAMA. ================== ')
print(f'Total da sua compra é de R${total:.2f}')
print(f'Temos {total1000} produtos custando mais de R$1000.00')
print(f'O Menor Preço foi de {barato} R$ {menorpreço:.2f}.')