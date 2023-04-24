n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
nota = (n1 + n2) / 2
if nota >= 7:
    print("Você Foi APROVADO com a nota {:.1f} !".format(nota))
elif 7 > nota >= 5:
    print('Você foi RECUPERAÇÃO com a nota {}'.format(nota))
elif nota < 5:
    print('Você foi REPROVADO COM A NOTA {}'.format(nota))