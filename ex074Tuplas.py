from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'os valores sorteados foram ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO Maior Numero sorteado foi {max(numeros)}')
print(f'O Menor Numero sorteado foi {min(numeros)}')