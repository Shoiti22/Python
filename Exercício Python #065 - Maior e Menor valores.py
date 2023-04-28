resp = 'S'
soma = cont = maior = menor = media = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja Continuar ? [S/N]'))
media = soma / cont
print('você digitou {} número e a média deles é {}'.format(cont, media))
print('Maior Número Digitado foi {} o menor foi {}'.format(maior, menor))

