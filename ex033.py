a = int(input('Primeiro Valor'))
b = int(input('Segundo Valor'))
c = int(input('Teceiro Valor'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando Maior Valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('Menor Valor foi {}'.format(menor))
print('Maior Valor foi {}'.format(maior))