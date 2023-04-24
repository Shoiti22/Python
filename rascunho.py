from time import sleep
from random import randint
#classe e raça.
print('''Bem Vindos a Vida Verdejante.
Uma Vila pequena aos arredores da Costa da Espada.''')

nome = str(input('Qual o Seu nome Héroi?'))
print('Sr.K : Muito prazer em conhecer {} Seja bem vindo a nossa Vila.'.format(nome))

#raça
print('''
Escolha a sua Raça:
[ 1 ] Para virar um HUMANO.
[ 2 ] Para virar um ELFO.
[ 3 ] Para virar um ORC.''')
raça = int(input('Sua Opção: '))
if raça == 1:
    print('Ótimo você escolheu ser um HUMANO.')
elif raça == 2:
    print('Ótimo você escolheu ser um ELFO.')
elif raça == 3:
    print('Ótimo você escolheu ser um ORC.')
else:
    print('Invalido tente novamente.')

#classe
print('''
Escolha a sua classe:
[ 1 ] Para virar um LADINO.
[ 2 ] Para virar um BARBARO.
[ 3 ] Para virar um GUERREIRO.''')
classe = int(input('Sua Opção: '))
if classe == 1:
    print('Ótimo você escolheu ser um LADINO.')
elif classe == 2:
    print('Ótimo você escolheu ser um BARBARO.')
elif classe == 3:
    print('Ótimo você escolheu ser um GUERREIRO.')
else:
    print('Invalido tente novamente.')

# Vidente.
print('''
Você esta andando pela cidade quando avista uma vidente ela pega sua mão e diz para jogarem um jogo de adivinhação.''')
vidente = randint(0, 10)
print('----- ela mexe com as mãos -------')
#sleep(2)
print('Vidente : Vou pensar em um número entre 0 e 5. Tente adivinhar...')
#sleep(3)
print('----- ela mexe com as mãos -------')
#sleep(2)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Em que número estou pensando?'))
    palpite += 1
    if jogador == vidente:
        acertou = True
    else:
        if jogador < vidente:
            print('Mais ... tente novamente.')
        elif jogador > vidente:
            print('Menos ... tente novamente.')
print('Eu Tinha pensando no numero {} você demorou {} Tentativas parabéns.'.format(vidente, palpite))