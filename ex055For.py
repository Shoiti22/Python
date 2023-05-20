maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª Pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O Maior peso lindo foi {}'.format(maior))
print('O Menor peso lido foi {}'.format(menor))
