print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro = int(input('Primeiro Termo:'))
razão = int(input('Razão da PA'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos mais você quer mostrar? '))
print('Foram mostrados {} termos mostrados.'.format(total))
print('FIM')