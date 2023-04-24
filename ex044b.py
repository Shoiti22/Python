print('Olá qual seria a forma de pagamento?')
print('===' * 20)
preço = float(input('Qual o Preço do Produto?'))
print('''FORMAS DE PAGAMENTO
[ 1 ] A VISTA DINHEIRO/CHEQUE
[ 2 ] A VISTA CARTÃO
[ 3 ] 2 X NO CARTÃO
[ 4 ] 3 X OU MAIS NO CARTÃO''')
opção = int(input('Qual é a Opção'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra sera parcelada em R${:.2f} de R${:.2f} COM JUROS'.format(totalparc,parcela))
else:
    total = 0
    print('Opção Invalida tente novamente.')
print('Sua compra de {:.2f} vai custar R${:.2f} no final'.format(preço, total))