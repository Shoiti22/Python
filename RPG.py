from time import sleep
#classe e raça
print('''\033[32m--- Bem Vindo a Porto Real --- 
O lar de muitos aventureiros Famosos
''')
sleep(3)

nome = str(input('Me Fale seu nome Héroi: '))
print('É uma honra ter você na cidade, {}.'.format(nome))

print('''
Escolha a sua Raça:
\033[32m[ 1 ]\033[m Para virar um HUMANO.
\033[32m[ 2 ]\033[m Para virar um ELFO.
\033[32m[ 3 ]\033[m Para virar um ORC.''')
raça = int(input('Sua Opção: '))
if raça == 1:
    print('\033[32mÓtimo você escolheu ser um\033[m \033[31mHUMANO.\033[m')
elif raça == 2:
    print('\033[32mÓtimo você escolheu ser um\033[m \033[31mELFO.\033[m')
elif raça == 3:
    print('\033[32mÓtimo você escolheu ser um\033[m \033[31mORC.\033[m')
else:
    print('\033[32mInvalido tente novamente.')
sleep(3)

#================================================================================================
print('''
\033[32mEscolha a sua classe:
[ 1 ]\033[m Para virar um LADINO.
\033[32m[ 2 ]\033[m Para virar um BARBARO.
\033[32m[ 3 ]\033[m Para virar um GUERREIRO.''')
classe = int(input('Sua Opção: '))
if classe == 1:
    print('\033[32mÓtimo você escolheu ser um\033[m \033[31mLADINO.\033[m')
elif classe == 2:
    print('\033[32mÓtimo você escolheu ser um\033[m \033[31mBARBARO.\033[m')
elif classe == 3:
    print('\033[32mÓtimo você escolheu ser um\033[m \033[31mGUERREIRO.\033[m')
else:
    print('\033[32mInvalido tente novamente.')
sleep(3)

#==================================================================================================================
# Vidente.
print('''
\033[32mVocê esta andando pela cidade quando avista uma vidente ela pega sua mão e diz para jogarem um jogo de adivinhação.
\033[m''')
from random import randint
vidente = randint(0, 5)
print('\033[34m----- ela mexe com as mãos -------\033[m')
sleep(2)
print('\033[33mVidente : Vou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
sleep(3)
print('\033[34m----- ela mexe com as mãos -------\033[m')
sleep(2)
jogador = int(input('\033[33mVidente : Em que Número eu Pensei? \033[m'))
if jogador == vidente:
    print('Você venceu eu pensei no número {}'.format(vidente))
else:
    print('\033[31mVocê perdeu eu pensei no {} e não no {}\033[m'.format(vidente, jogador))
sleep(3)
print('''\033[32mEla Se vira e vai embora para sua barraca que esta ali perto\033[m \033[31mGRITA : PERDEDOR !!!!\033[m
''')
sleep(3)
print('''\033[32mVocê segue seu caminho andando pela rua quando da de frente com um
\033[m 
\033[33mMendingo: que começa a falando que achou um jogo legal que vem do
oriente gostaria de tentar ? Aposto 10 Moedas.\033[m''')
sleep(3)
print('''
\033[32m[ 1 ]\033[m ACEITAR
\033[32m[ 2 ]\033[m RECUSAR''')
joken = int(input('Sua Opção: '))
if joken == 1:
    print('\033[33mVamos Começar !!! jogo se chama JO-KEN-PO mas conhecido como PEDRA, PAPEL, TESOURA\033[m')
elif joken == 2:
    print('\033[33mVocê tem cara de perdedor mesmo.\033[m')