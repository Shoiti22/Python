lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um Valor : ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-=' * 30)
print(f'Esses foram todos os valores digitados. {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores impares digitados foram: {impar}')
print('')