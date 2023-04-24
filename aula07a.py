#ex5 13/02
n = int(input('digite um número.'))
#a = n - 1
#s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))

#ex6 13/02
n = int(input('digite um numero'))
#d = n * 2
#t = n * 3
#p = n ** (1/2)
print('o dobro de {} é {} \n O Triplo é {} \n O cubico é {:.2f} !'.format(n, (n*2), (n*3), (n**(1/2))))

#ex7 13/02
nota = float(input('Digite a Nota.'))
nota2 = float(input('Digite a Segunda Nota.'))
m = (nota+nota2)/2
#r = m / 2
print('A nota media entre {:.1f} e {:.1f} do aluno é {:.1f}'.format(nota, nota2, m))

#ex08 13/02
a = float(input('Digite Quantos Metros?'))
print('O Valor em Metro é {}'.format(a))
#km = a/1000
#hm = a/100
#dam = a/10
#dm = a*10
#cm = a*100
#mm = a*1000
#print("{} km\n{} hm\n{} dam\n{} dm\n{} cm\n{:.1f} mm".format(km, hm, dam, dm, cm, mm))

print('{} km\n{} hm\n{}dam \n{} dm\n{} cm\n{} mm'.format((a/1000), (a/100), (a/10), (a*10), (a*100), (a*1000)))

#ex09 14/02 tabuada
t = int(input('Digite para saber Tabuada.'))
t1 = t*1
t2 = t*2
t3 = t*3
t4 = t*4
t5 = t*5
t6 = t*6
t7 = t*7
t8 = t*8
t9 = t*9
t10 = t*10
print('Valor\n{}x1={}\n{}x2={}\n{}x3={}\n{}x4={}\n{}x5={}\n{}x6={}\n{}x7={}\n{}x8={}\n{}x9={}\n{}x10={}'
      .format(t, t1, t, t2, t, t3, t, t4, t, t5, t, t6, t, t7, t, t8, t, t9, t, t10))
#print('{} x {} = {}'.format(t, t*1))

#ex010 14/02 conversão de real para dolar.
c = float(input('quanto de dinheiro você tem na carteira? R$'))
d = c/3.27

print('Com R${:.2f} você pode comprar US$ {:.2f}.'.format(c,d))

#ex011 15/02 quantos de tinta usariamos na parede.
largura = float(input('Largura? '))
altura = float(input('Altura? '))
metros = float(largura * altura)*1000
tinta = float(metros / 2)

print('Sua Parede tem {} x {} e sua área é de {:.0f}m².'.format(largura, altura, metros))
print('Para pintar sua parede, você precisa de {}l de tinta'.format(tinta))

#ex012 15/02 desconto
produto = float(input('Qual é o preço do produto? R$'))
valorbruto = (produto * 5) / 100
desconto = valorbruto - produto
print('O Produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(produto,desconto))


#ex013 15/02 aumento de salario.
salario = float(input('Digite Seu Salario'))
base = (salario * 15) / 100
Aumento = base + salario
print('O Salario Atual é de {:.2f} com aumento de 15% é {:.2f}'.format(salario, Aumento))

#ex014 17/02
