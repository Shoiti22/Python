def area(l, c):
    a = l * c
    print(' ---  CONTROLE DE TERRENOS ---  ')
    print('--------------------------------')
    print(f'A área de um terreno {l} x {c} é de {a}m².')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

========================================================================================

def escreva(txt):
    t = len(txt)+4
    print('-' * t)
    print(f'{txt:^{t}}')
    print('-' * t)

#Program Principal.
escreva('Oi')
escreva('Maneiro mewwwww')

========================================================================================

from time import sleep

def contador(i, f, p):
    print('-=' * 8)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.4)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='..')
            sleep(0.4)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='..')
            sleep(0.4)
            cont -= p
        print('FIM')
    print('-=' * 8)


#Programa Principal.
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 8)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:'))
pas = int(input('Passo: '))
contador(ini, fim, pas)