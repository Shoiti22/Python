soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite os numeros'))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} Números pares resultado deu {}'.format(cont, soma))