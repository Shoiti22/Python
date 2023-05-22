lista = list()
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR? S/N ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-' * 30)
print(f'Você Digitou {cont} Elementos.') # O CERTO ERA USAR {len(lista)} no lugar dessa cont.
lista.sort(reverse=True)
print(f'Os Valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O Valor 5 faz parte da lista.')
else:
    print('O Valor 5 Não faz parte da lista.')