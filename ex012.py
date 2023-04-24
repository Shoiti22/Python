produto = float(input('Qual é o preço do produto? R$'))
valorbruto = (produto * 5) / 100
desconto = valorbruto - produto
print('O Produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(produto,desconto))