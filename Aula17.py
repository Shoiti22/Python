# a lista você pode substituir algo ex na chave lanche = ['hamburger', 'suco', 'pizza', 'pudim']
# se eu colocar lanche[3] = 'Picolé' ele substitui o pudim pelo picolé.
# com o comando lanche.append('cookie') eu consigo adicionar mais coisas ex ['hamburger', 'suco', 'pizza', 'picolé', 'cookie']
# com o comando lanche.insert(0, 'hotdog') ele ira adicionar na frente ex  ['hotdog', 'hamburger', 'suco', 'pizza', 'picolé', 'cookie']
# com comando del lanche[3] e lanche.pop(3) se quiser pelo contéudo lanche.remove('pizza') elimina um elimento e reposiona a contagem ex ['hotdog', 'hamburger', 'suco', 'picolé', 'cookie']
#outro comando que podemos usar é valores.sort(reverse=True) para botar em ordem de traz para frente.

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')
 

=======================================================

valores = list()
for cont in range(0, 5):
    valores.append((int(input('Digite um valor'))))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}! ')
print('Chegue ao final da lista.')

=======================================================

a = [2, 3, 4, 7]
b = a[:]    #esse comando é pra fazer uma copia de a para b caso contrario elas ficam ligadas.
b[2] = 8
print(f'Lista A {a}')
print(f'Lista B {b}')