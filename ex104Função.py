def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO DIGITE UM NÚMERO INTEIRO VALIDO.\033[m')
        if ok:
            break
    return valor


#Programa Principal
n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar  o número {n}')