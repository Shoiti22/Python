from random import randint
computador = randint(0, 5) #FAZ O COMPUTADOR PENSAR. OU SORTEAR
print('---' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('---' * 20)
jogador = int(input('Em que Número eu Pensei?'))# JOGADOR TENTA ADIVINHAR
if jogador == computador:
    print('Você Venceu eu pensei no número {}'.format(computador))
else:
    print('Ganhei, eu pensei em numero {} e Não no {}!'.format(computador, jogador))

