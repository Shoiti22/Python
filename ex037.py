num= int(input('Digite um numero. '))
print('''Escolha uma das base para conversão:
[ 1 ] converter para BINARIO.
[ 2 ] converter para OCTAL.
[ 3 ] converter para HEXADECIMAL.''')
opção = int(input('Sua Opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXDECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Invalida. tente novamente')