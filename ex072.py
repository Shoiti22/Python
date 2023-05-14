cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
        'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    núm = int(input('Digite um numero de 0 a 20 '))
    respo = ' '
    if 0 <= núm <= 20:
        print(f'Você digitou o número {cont[núm]}')
    print('Tente novamente de 0 a 20', end= ' ')
    while respo not in ('S/N'):
        respo = str(input('Quer Continuar?')).strip().upper()[0]
    if respo == 'N':
        break
print('Programa finalizado obrigado')