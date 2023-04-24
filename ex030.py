numero = int(input('Digite um numero qualquer: '))
resultado = numero % 2
print('O Resultado do Numero é {}'.format(resultado))
if resultado == 0:
    print('O Seu Numero {} é Par'.format(numero))
else:
    print('Esse Número {} é Impar'.format(numero))