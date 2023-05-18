núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite ultimo número: ')))
print(f'Você digitou os valores {núm}')
print(f'O Valor 9 apareceu {núm.count(9)} Vezes')
if 3 in núm:
    print(f'O Valor 3 apareceu na {núm.index(3)+1} posição')
else:
    print('O Valor 3 Não foi digitado')
print(f'Os Valores apares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')