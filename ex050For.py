soma = 0
cont = 0
for c in range(1, 5):
    num = int(input('Digite os valores: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'O Total de Número foi {cont} somando eles o valor total ficou {soma}')