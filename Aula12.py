nome = str(input('Qual o seu nome?'))
if nome == 'Shoiti':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo Nome Feminino')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}.'.format(nome))

#ex 042
print('Analisando um Triangulo: ')
print('=====' * 20)
a = float(input('Primeiro Segmento:'))
b = float(input('Segundo Segmento:'))
c = float(input('Terceiro Segmento:'))
if a < b + c and b < a + c and c < a + b:
    print('Os Seguimentos podem formar um triangulo! ', end= '')
    if a == b == c:
        print('EQUILATERO')
    if a != b != c != a:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Os Segmentos a cima não formam um triangulo.')