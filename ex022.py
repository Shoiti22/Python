nome = str(input('Digite seu Nome.')).strip()
divido = nome.split()
print('analisando seu nome')
print('Seu Nome é em Maiúsculo {}'.format(nome.upper()))
print('Seu Nome em Minúsculo é {}'.format(nome.lower()))
print('Seu Nome tem o total de {}'.format(len(nome) - nome.count(' ')))
print('Seu Primeiro Nome é {} e possui {} Letras'.format(divido[0], len(divido[0])))