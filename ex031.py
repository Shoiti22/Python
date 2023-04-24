viagem = float(input('Qual a Distancia da viagem ? '))
if viagem > 200:
    print('Você vai pagar 0.45 por KM por viagens a cima de 200 KM')
    viagem1 = (viagem * 0.45)
    print('O Preço de sua passagem sera R${:.2f} '.format(viagem1))
else:
    viagem2 = (viagem * 0.50)
    print('O Preço de sua passagem sera R${:.2f} '.format(viagem2))