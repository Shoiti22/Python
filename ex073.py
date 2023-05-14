times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Atletico-PR', 'Cruzeiro', 'Fortaleza', 'Sao Paulo', 'Atletico-MG',
         'Santos', 'Gremio', 'Internacional', 'Flamengo', 'Bahia', 'Vasco da Gama', 'Bragantino', 'Corinthians', 'Cuiaba',
         'Goiais', 'Curitiba', 'America-MG')

print(f'Lista de times Brasileirao: {times}')
print('=-=-' * 20)
print(f'Os 5 Primeiros Time do Brasileirao sao {times[0:5]}')
print('=-=-' * 20)
print(f'Os 4 Ultimos Time do Brasileirao sao {times[16:20]}')
print('=-=-' * 20)
print('Em Ordem Alfabetica', end= ' ')
print(sorted(times))
print('=-=-' * 20)
print(times.index(1))
