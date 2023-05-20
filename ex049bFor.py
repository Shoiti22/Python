#faça a tabuada
num = int(input('Digite um número:'))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))