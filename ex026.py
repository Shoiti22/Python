frase = str(input('Digite Uma Frase.')).upper().strip()
print('A letra A Aparece {} Vezes na frase'.format(frase.count('A')))
print('A Primeira Letra A Apareceu na Posição {}'.format(frase.find('A')+1))
print('A Ultima Letra A aparece na posição {}'.format(frase.rfind('A')+1))