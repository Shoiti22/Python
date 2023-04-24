print('Analisando um Triangulo')
print('=====' * 20)
a = float(input('Primeiro Segmento'))
b = float(input('Segundo Segmento'))
c = float(input('Terceiro Segmento'))
if a < b + c and b < a + c and c < a + b:
    print('Os Seguimento a cima podem formar um triangulo')
else:
    print('Não podem formar triangulo')