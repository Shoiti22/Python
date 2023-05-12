
#exemplos
n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota : '))
m = (n1 + n2)/2
print('A Sua Media é foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua media foi boa')
else:
    print('Sua Media foi ruim')

# exemplos
    nome = str(input('Qual é o seu nome?'))
    if nome == 'Renan':
        print('Que nome lindo você tem!')
    else:
        print('Nome é tão Normal')
    print('Bom Dia, {}'.format(nome))

    # exemplos

    tempo = int(input('Quantos Anos tem seu carro?'))
    if tempo <= 3:
        print('Carro Novo ')
    else:
        print('Carro Velho')
    print('--Fim--')

#exec 28

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



#exec 29
velocidade = float(input('Qual é a velocidade do carro?'))
if velocidade > 80:
    print('MULTADO! Você Excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R#{:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança')

#exec 30

numero = int(input('Digite um numero qualquer: '))
resultado = numero % 2
print('O Resultado do Numero é {}'.format(resultado))
if resultado == 0:
    print('O Seu Numero {} é Par'.format(numero))
else:
    print('Esse Número {} é Impar'.format(numero))

#exec 31

viagem = float(input('Qual a Distancia da viagem ? '))
if viagem > 200:
    print('Você vai pagar 0.45 por KM por viagens a cima de 200 KM')
    viagem1 = (viagem * 0.45)
    print('O Preço de sua passagem sera R${:.2f} '.format(viagem1))
else:
    viagem2 = (viagem * 0.50)
    print('O Preço de sua passagem sera R${:.2f} '.format(viagem2))

#exec 32

from datetime import date
ano = int(input('Que ano você quer analisar ? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISEXTO'.format(ano))
else:
    print('O Ano {} Não é BISEXTO'.format(ano))

#exec 33

a = int(input('Primeiro Valor'))
b = int(input('Segundo Valor'))
c = int(input('Teceiro Valor'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando Maior Valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('Menor Valor foi {}'.format(menor))
print('Maior Valor foi {}'.format(maior))

#exec 34

salario = float(input('Digite Salario: '))
if salario <= 1250:
    aumento = (salario * 15 / 100) + salario
else:
    aumento = (salario * 10 / 100) + salario
print('Você Recebia R$ {:.2f} e agora Recebe {:.2f} Salario'.format(salario, aumento))

