from datetime import date
atual = date.today().year
nasc = int(input('Qual ano de nascimento: '))
idade = atual - nasc
print('Então você tem {} Anos'.format(idade))
if idade <= 9:
    print('Você é da categoria MIRIM')
elif idade <= 14:
    print('Você é da categoria INFANTIL')
elif idade <= 19:
    print('Você é da categoria JUNIOR')
elif idade <= 25:
    print('Você é da categoria SENIOR')
else:
    print('Você é da categoria MASTER')