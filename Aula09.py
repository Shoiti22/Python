#Exec 22
nome = str(input('Digite seu Nome.')).strip()
divido = nome.split()
print('analisando seu nome')
print('Seu Nome é em Maiúsculo {}'.format(nome.upper()))
print('Seu Nome em Minúsculo é {}'.format(nome.lower()))
print('Seu Nome tem o total de {}'.format(len(nome) - nome.count(' ')))
print('Seu Primeiro Nome é {} e possui {} Letras'.format(divido[0], len(divido[0])))

#Exec 23

numero = int(input('Informe Um Numero'))
n = str(numero)
print('Analisando o Numero {} ...'.format(numero))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

#Exec 23 Segunda Forma de Fazer. forma certa !!!!

numero = int(input('Informe Um Numero'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o Numero {} ...'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#exec 24

nome = str(input('Em Que Cidade você nasceu?')).strip()
print(nome[:5].upper() == 'SANTO')

#print('Santo'in nome)

#exec 25
nome = str(input('Qual o Seu Nome?')).strip()
print('Seu Nome Tem Silva? {}'.format('SILVA' in nome.upper()))

#exec 26

frase = str(input('Digite Uma Frase.')).upper().strip()
print('A letra A Aparece {} Vezes na frase'.format(frase.count('A')))
print('A Primeira Letra A Apareceu na Posição {}'.format(frase.find('A')+1))
print('A Ultima Letra A aparece na posição {}'.format(frase.rfind('A')+1))

#exec 27

nome = str(input('Digite Seu Nome Completo:')).strip().split()
print('Muito Prazer em te conhecer')
print('Seu Primeiro Nome é {}'.format(nome[0]))
print('Seu Ultimo Nome é {}'.format(nome[-1]))

