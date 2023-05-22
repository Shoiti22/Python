lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')

#print(sorted(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f' Eu vou comer {comida} na posição {pos}')
print('Comida pra Caramba.')

#----------------------------------------------------------------------------------------------------------

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(4))
#elas se soma no caso fica (2 5 4) que seria a + b (5 8 1 2) ficando (2 5 4 5 8 1 2) sem somar so juntando.

#-----------------------------------------------------------------------------------------------------------

print('===== BANCO NSO =====!!==')
valor = int(input('QUAL VALOR VOCÊ DESEJA SACAR ? R$'))
total = valor
nota = 50
totalnota = 0
while True:
    if total >= nota:
        total -= nota
        totalnota += 1
    else:
        if totalnota > 0:
            print(f'Total de {totalnota} Notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalnota = 0
        if total == 0:
            break
print('ACABOU')

#-----------------------------------------------------------------------------------------------------------

times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Atletico-PR', 'Cruzeiro', 'Fortaleza', 'Sao Paulo', 'Atletico-MG',
         'Santos', 'Gremio', 'Internacional', 'Flamengo', 'Bahia', 'Vasco da Gama', 'Bragantino', 'Corinthians', 'Cuiaba',
         'Goiais', 'Curitiba', 'America-MG')

print(f'Lista de times Brasileirao: {times}')
print('=-=-' * 20)
print(f'Os 5 Primeiros Time do Brasileirao sao {times[0:5]}')
print('=-=-' * 20)
print(f'Os 4 Ultimos Time do Brasileirao sao {times[16:20]}') # ou -4
print('=-=-' * 20)
print(f'Em Ordem Alfabetica {sorted(times)}') # pode usar o sorted assim.
print('=-=-' * 20)
print(f'O Flamengo esta na {times.index("Flamengo")+1} posição') # para arrumar possição e como usar o index certo.

#-----------------------------------------------------------------------------------------------------------

#ex 073 para fazer mais de um sorteio de numero tem que colocar o ( no randint e fechar ) usar comando MAX e MIN para saber valor mais alto e mais baixo
from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), )
print(f'os valores sorteados foram ', end='')
for n in numeros:
    print(f'{n}', end='')
print(f'\nO Maior Numero sorteado foi {max(numeros)}') #maior valor
print(f'O Menor Numero sorteado foi {min(numeros)}') # menor valor.

#-----------------------------------------------------------------------------------------------------------

#ex075

n1 = int(input('Digite um número.'))        #dificuldade aqui que ele fez em tuplas eu fiz errado.
n2 = int(input('Outro número'))
n3 = int(input('mais um número'))
n4 = int(input('Último número'))
total = n1, n2, n3, n4
print(f'Você digitou os valores {total}')
print(f'O Valor 9 apareceu {total.count(9)} Vezes')
if 3 in total:
    print(f'O Valor 3 apareceu na {total.index(3)} posição')
else:
    print('O Valor 3 Não foi digitado')
print(f'Os Valores apares digitados foram ', end='')
for n in total:
    if n % 2 == 0:
        print(n, end=' ')

resposta do exercicio feito #modo de tuplas certo. ex075

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

#-----------------------------------------------------------------------------------------------------------

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Compasso', 10.00,
            'Mochila', 120.00)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')  #duvidas de como usar o par e impar pós % 2 == 0:
    else:
        print(f'R${listagem[pos]:>7.2f}')


#tuplas são imutaveis.

#comandos novos.
#enumerate para numerar.
#sorted para organizar. ordem alfabetica. reverse=True
#index

#isso é uma tupla ()
#isso é uma lista []
#isso é um dicionario {}