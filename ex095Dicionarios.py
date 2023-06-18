time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'         Quantos Gols na partida {c+1} ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer Continuar? S/N ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda somente com S ou N.')
    if resp == 'N':
        break
print('-' * 40)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print('Não existe jogador com esse codigo.{busca}!')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'       No Jogo {i+1} Fez {g} Gols.')
    print('-' * 40)
print('Volte Sempre.')