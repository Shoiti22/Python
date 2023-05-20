num = cont = soma = 0
num = int(input('Digite um Número e [999 para parar] '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um Número e [999 para parar] '))
print('FIM você digitou {} e total foi {} '.format(cont, soma))