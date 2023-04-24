largura = float(input('Largura? '))
altura = float(input('Altura? '))
metros = float(largura * altura)*1000
tinta = float(metros / 2)

print('Sua Parede tem {} x {} e sua área é de {:.0f}m².'.format(largura, altura, metros))
print('Para pintar sua parede, você precisa de {}l de tinta'.format(tinta))