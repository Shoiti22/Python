n = int(input('Digite um numero'))
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(1, n+1,):
    print('{}'.format(c), end='')
    print(' x ' if c > 0 else ' = ', end='')
    f *= c
print('{}'.format(f))