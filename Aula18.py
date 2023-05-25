galera = list()
dados = list()
dados = list() #aula 18 ou 17 parte 2 de listas dentro de lista.
pessoas = list()
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(30)
print(dados[0])
print(dados[1])
pessoas.append(dados[:])
print(pessoas)
print(pessoas[1][1])

=========================================================================

teste = list()
teste.append('Shoiti')
teste.append(30)
galera = list()
galera.append(teste[:]) # sempre lembrar de colocar o [:] pois significa que é uma copia se não ele duplica na de baixo.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #sempre colocar em ambos, o [:]
print(galera)

==========================================================================

galera = [['João', 19], ['Ana', 19], ['Fernanda', 25], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} Anos de idade.')

==========================================================================

galera = list()
dados = list()
totalmai = totalmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome:')))
    dados.append((int(input('Idade: '))))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmai += 1
print(f'Temos {totalmai} maior de idade e temos {totalmen} menor de idade.')