numero = int(input('Digite um numero: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c ==0:
        tot += 1
        print('\033[31m', end='')
    else:
        print('\033[33m',end='')
    print('{}'.format(c), end=' ')
print('\n\033[m numero {} foi dividido {} vezes'.format(numero, tot))
if tot == 2:
    print('esse é primo')
else:
    print('Não é Primo')
