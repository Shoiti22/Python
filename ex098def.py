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