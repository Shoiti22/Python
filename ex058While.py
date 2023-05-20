from random import randint
computador = randint(0, 10) #FAZ O COMPUTADOR PENSAR. OU SORTEAR
print('---' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('---' * 20)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Em que Número eu estou pensando? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print('Eu pensei no numero {} foram {} tentativas para acerta'.format(computador, palpite))