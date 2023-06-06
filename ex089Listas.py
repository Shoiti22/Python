ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{ficha}')