from random import randint
v = 0
while True:
    jogador = int(input('Digite um Valor'))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in ('PpIi'):
        tipo = str(input('Par ou Impar ?')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Ganhou')
            v += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Ganhou')
            v += 1
        else:
            print('Você Perdeu')
            break
    print('Jogar novamente....')
print(f'GAME OVER Você Venceu {v} vezes.')