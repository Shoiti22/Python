from datetime import date
cont = 0
cont1 = 0
for c in range(1, 8):
    nasc = int(input('Digite seu ano de nascimento.'.format(c)))
    atual = date.today().year
    idade = (atual - nasc)
    if idade >= 18:
        cont += 1
        print('Você é um maior de {} anos e {}'.format(idade, cont))
    elif idade <=18:
        cont1 += 1
        print('Você é menor de {} anos e {}'.format(idade, cont1))
print('''Ao todo tivemos {} maior de idade
e tivemos também {} menor de idade.'''.format(cont, cont1))