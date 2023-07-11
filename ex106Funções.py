c = ('\033[m',       # 0 - sem cores.
     '\033[0;30;41m',  # 1 - vermelho.
     '\033[0;30;42m',  # 2 - verde.
     '\033[0;30;43m'  # 3 - amarelo.
     );

def ajuda(com):
    help(com)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')


#Programa Principal
comando = ''
while True:
    título('Sistema De Ajuda Pyhelp', 2)
    comando = str(input("Função Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até Logo', 1)