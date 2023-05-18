times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Atletico-PR', 'Cruzeiro', 'Fortaleza', 'Sao Paulo', 'Atletico-MG',
         'Santos', 'Gremio', 'Internacional', 'Flamengo', 'Bahia', 'Vasco da Gama', 'Bragantino', 'Corinthians', 'Cuiaba',
         'Goiais', 'Curitiba', 'America-MG')

print(f'Lista de times Brasileirao: {times}')
print('=-=-' * 20)
print(f'Os 5 Primeiros Time do Brasileirao sao {times[0:5]}')
print('=-=-' * 20)
print(f'Os 4 Ultimos Time do Brasileirao sao {times[16:20]}') # ou -4
print('=-=-' * 20)
print(f'Em Ordem Alfabetica {sorted(times)}')
print('=-=-' * 20)
print(f'O Flamengo esta na {times.index("Flamengo")+1} posição')
