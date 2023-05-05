from datetime import date

idade = 0 #mais de 18 anos
totalhomens = 0 #quantos homens foram cadastrados.
mulheres = 0 #mulheres menos de 18 anos.
total = 0 #total pessoas maiores de 18
resposta = 0
while True:
    idade = int(input('IDADE :'))
    sexo = ' '
    while sexo not in ('MF'):
        sexo = str(input('[M/F]')).strip().upper()[0]
    resposta = ' '
    while resposta not in ('SN'):
        resposta = str(input('Quer Continuar?')).strip().upper()[0]
    if resposta == 'N':
        break
    if idade > 18:
        total += 1
    if sexo == 'M':
        totalhomens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
print(f'Total de pessoas com mais de 18 anos foi {total}')
print(f'Total de Homens cadastrados {totalhomens}')
print(f'Total de Mulheres com menos de 20 anos foi {mulheres}')