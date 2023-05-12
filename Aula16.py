lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')

#print(sorted(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f' Eu vou comer {comida} na posição {pos}')
print('Comida pra Caramba.')

#----------------------------------------------------------------------------------------------------------

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(4))
#elas se soma no caso fica (2 5 4) que seria a + b (5 8 1 2) ficando (2 5 4 5 8 1 2) sem somar so juntando.

#-----------------------------------------------------------------------------------------------------------

#tuplas são imutaveis.

#comandos novos.
#enumerate para numerar.
#sorted para organizar. ordem alfabetica.
#index

#isso é uma tupla ()
#isso é uma lista []
#isso é um dicionario {}