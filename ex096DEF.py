def area(l, c):
    a = l * c
    print(' ---  CONTROLE DE TERRENOS ---  ')
    print('--------------------------------')
    print(f'A área de um terreno {l} x {c} é de {a}m².')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
