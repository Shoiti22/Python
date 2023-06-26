def ficha(jog='<desconhecido>', gol=0):
    print(f'Jogador {jog} Fez {gol} gols no campeonato.')


#Programa Principal.
n = str(input('Nome do Jogador: '))
g = str(input('Quantos Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)