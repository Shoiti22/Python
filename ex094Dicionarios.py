galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO DIGITE APENAS M OU F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer Continuar? S/N ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda somente com S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f'B) A Média de idade é de {média:5.2f} Anos')
print('C) A mulheres cadastradas foram ', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()
print(f'Lista das pessoas acima da média')
for p in galera:
    if p['idade'] >= média:
        print('       ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>>')


#print(galera) #assim ele salva todos os dados dentro de um dicionario.
#print(pessoa) #assim ele só salva o ultimo dado.