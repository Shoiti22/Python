print('Olá qual seria a forma de pagamento?')
print('===' * 20)
produto = float(input('Qual o Preço do Produto?'))
print('[1]DINHEIRO A VISTA.')
avista = (produto * 10 / 100)
a = (produto - avista)
print('[2]CARTÃO DE CREDITO.')
credito = (produto * 5 / 100)
b = (produto - credito)
print('[3]2X CARTÃO.')
normal = (produto / 2)
c = (produto)
print('[4]3X DA 20% DE JUROS.')
juros = produto +(produto * 20 / 100)
d = (produto)
e = (juros / 3)
pagamento = int(input('Qual seria a forma de pagamento?'))
if pagamento == 1:
    print('O Desconto do produto é R${:.2f} ficando valor de R${:.2f}'.format(avista, a))
elif pagamento == 2:
    print('O Desconto do produto é R${:.2f} ficando no valor de R${:.2f}'.format(credito, b))
elif pagamento == 3:
    print('Valor da parcela ficou 2 X R${:.2f} do valor total de R${:.2f}'.format(normal, c))
elif pagamento == 4:
    print('Valor do produto ficou 20% mais caro, R${} do valor total R${}. A PARCELA FICOU 3X DE R${}'.format(juros))